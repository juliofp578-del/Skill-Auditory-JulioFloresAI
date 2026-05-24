"""
Weekly AI Newsletter - Resumen semanal de noticias de IA empresarial.
Se ejecuta automáticamente cada domingo a las 20:00 hora España (18:00 UTC / CEST)
via GitHub Actions.
"""

import html
import os
import re
import smtplib
import socket
import traceback
import feedparser
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import anthropic

# Timeout global para peticiones de red (segundos)
socket.setdefaulttimeout(15)

RSS_FEEDS = [
    ("Google AI Blog",        "https://blog.google/technology/ai/rss/"),
    ("Google DeepMind",       "https://deepmind.google/blog/rss.xml"),
    ("OpenAI Blog",           "https://openai.com/news/rss.xml"),
    ("Anthropic News",        "https://www.anthropic.com/news/rss.xml"),
    ("MIT Tech Review AI",    "https://www.technologyreview.com/topic/artificial-intelligence/feed/"),
    ("VentureBeat AI",        "https://venturebeat.com/category/ai/feed/"),
    ("TechCrunch AI",         "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("The Verge AI",          "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"),
    ("Ars Technica AI",       "https://feeds.arstechnica.com/arstechnica/index"),
    ("Wired AI",              "https://www.wired.com/feed/tag/ai/latest/rss"),
    ("Reuters Technology",    "https://feeds.reuters.com/reuters/technologyNews"),
    ("Bloomberg Technology",  "https://feeds.bloomberg.com/technology/news.rss"),
]

SYSTEM_PROMPT = """Eres un analista experto en inteligencia artificial y tecnología empresarial.
Tu misión es crear resúmenes semanales ejecutivos, claros y accionables sobre el ecosistema de IA,
con foco especial en Google, Anthropic, OpenAI y la aplicación empresarial de la IA.
Escribes en español, con un estilo profesional pero accesible. Nunca inventas noticias.
Cuando no hay noticias de una empresa o sección, lo indicas claramente."""


def _strip_html(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_week_articles() -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    articles = []

    for source_name, feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            count_added = 0
            for entry in feed.entries[:20]:
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

                if published and published < cutoff:
                    continue

                title = _strip_html(entry.get("title", "Sin título"))
                summary = _strip_html(entry.get("summary", entry.get("description", "")))[:700]

                articles.append({
                    "source": source_name,
                    "title": title,
                    "summary": summary,
                    "link": entry.get("link", ""),
                    "published": published.strftime("%d/%m/%Y") if published else "N/A",
                })
                count_added += 1

            print(f"[INFO] {source_name}: {count_added} artículos de la semana (total feed: {len(feed.entries)})")
        except Exception as exc:
            print(f"[WARN] {source_name}: {exc}")

    print(f"[INFO] Total artículos recopilados: {len(articles)}")
    return articles[:50]


def generate_newsletter_html(articles: list[dict]) -> str:
    client = anthropic.Anthropic()

    articles_text = "\n\n".join(
        f"[{a['source']} · {a['published']}]\nTítulo: {a['title']}\nResumen: {a['summary']}\nURL: {a['link']}"
        for a in articles
    )

    week_start = (datetime.now() - timedelta(days=6)).strftime("%d/%m/%Y")
    week_end = datetime.now().strftime("%d/%m/%Y")
    week_range = f"{week_start} – {week_end}"

    print("[INFO] Llamando a Claude API (claude-sonnet-4-6)...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{
            "role": "user",
            "content": f"""Genera el HTML completo de un newsletter semanal de IA empresarial.

SEMANA: {week_range}

NOTICIAS RECOPILADAS:
{articles_text}

INSTRUCCIONES DE FORMATO:
- HTML completo con estilos CSS inline (compatible con clientes de email, sin <style> en <head>).
- Diseño oscuro y profesional: fondo #0f0f1a, texto #e2e8f0, acentos en #6366f1 (índigo).
- Fuente: Arial, sans-serif. Ancho máximo 680px, centrado con margin:auto.
- Estructura obligatoria (en este orden):

  1. HEADER — Logo/título "🤖 AI Weekly" en grande + subtítulo "Semana del {week_range}" en color índigo.

  2. RESUMEN EJECUTIVO — Caja destacada con los 5 puntos más importantes de la semana en bullets.

  3. 🔵 GOOGLE & DEEPMIND — Noticias con título clicable, fuente y fecha.

  4. 🟣 ANTHROPIC — Noticias con título clicable, fuente y fecha.

  5. 🟢 OPENAI — Noticias con título clicable, fuente y fecha.

  6. 🏢 IA EN EMPRESAS — Casos de adopción empresarial, inversiones, estrategias corporativas.

  7. 🚀 MODELOS & PRODUCTOS — Nuevos lanzamientos, actualizaciones de modelos.

  8. 📡 EN EL RADAR — Tendencias emergentes y temas para seguir.

  9. FOOTER — "Generado automáticamente con Claude Sonnet · {week_range}" en texto pequeño gris.

- Cada noticia: título como enlace <a href="..."> en color #818cf8, descripción breve de 1-2 líneas.
- Si no hay noticias de una sección: "Sin novedades esta semana." en cursiva.
- Solo HTML con estilos inline. Sin JavaScript. Sin <script>. Sin imágenes externas.""",
        }],
    )

    html_content = response.content[0].text
    print(f"[INFO] HTML generado: {len(html_content)} caracteres")
    return html_content


def send_email(html_body: str) -> None:
    gmail_user = os.environ["GMAIL_USER"]
    gmail_password = os.environ["GMAIL_APP_PASSWORD"]
    recipient = os.environ["RECIPIENT_EMAIL"]

    week_str = datetime.now().strftime("%d/%m/%Y")
    subject = f"🤖 AI Weekly · Resumen IA empresarial · semana del {week_str}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"AI Weekly Newsletter <{gmail_user}>"
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    print(f"[INFO] Conectando a smtp.gmail.com:465 → enviando a {recipient}...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient, msg.as_string())

    print(f"[OK] Newsletter enviado correctamente a {recipient}")


def main() -> None:
    print(f"[START] {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} — Generando newsletter semanal de IA...")

    try:
        articles = fetch_week_articles()
    except Exception:
        print("[ERROR] Error al obtener artículos RSS:")
        traceback.print_exc()
        raise

    if not articles:
        print("[WARN] Sin artículos esta semana — usando mensaje de aviso.")
        articles = [{
            "source": "Sistema",
            "title": "No se encontraron noticias esta semana",
            "summary": "Los feeds RSS no devolvieron artículos en los últimos 7 días.",
            "link": "",
            "published": datetime.now().strftime("%d/%m/%Y"),
        }]

    try:
        html_content = generate_newsletter_html(articles)
    except Exception:
        print("[ERROR] Error al generar el HTML con Claude:")
        traceback.print_exc()
        raise

    try:
        send_email(html_content)
    except Exception:
        print("[ERROR] Error al enviar el email:")
        traceback.print_exc()
        raise

    print("[DONE] Newsletter completado exitosamente.")


if __name__ == "__main__":
    main()
