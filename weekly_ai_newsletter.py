"""
Weekly AI Newsletter - Resumen semanal de noticias de IA
Se ejecuta automáticamente cada domingo a las 20:00 via GitHub Actions.
"""

import os
import smtplib
import traceback
import feedparser
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import anthropic

RSS_FEEDS = [
    ("Google AI Blog",     "https://blog.google/technology/ai/rss/"),
    ("OpenAI Blog",        "https://openai.com/news/rss.xml"),
    ("Anthropic News",     "https://www.anthropic.com/news/rss.xml"),
    ("MIT Tech Review AI", "https://www.technologyreview.com/topic/artificial-intelligence/feed/"),
    ("VentureBeat AI",     "https://venturebeat.com/category/ai/feed/"),
    ("TechCrunch AI",      "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("The Verge AI",       "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"),
    ("Ars Technica AI",    "https://feeds.arstechnica.com/arstechnica/index"),
]

SYSTEM_PROMPT = """Eres un analista experto en inteligencia artificial y tecnología empresarial.
Tu misión es crear resúmenes semanales ejecutivos, claros y accionables sobre el ecosistema de IA,
con foco especial en Google, Anthropic, OpenAI y la aplicación empresarial de la IA.
Escribes en español, con un estilo profesional pero accesible. Nunca inventas noticias."""


def fetch_week_articles() -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    articles = []

    for source_name, feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            print(f"[INFO] {source_name}: {len(feed.entries)} entradas")
            for entry in feed.entries[:15]:
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                if published and published < cutoff:
                    continue
                articles.append({
                    "source": source_name,
                    "title": entry.get("title", "Sin título").strip(),
                    "summary": entry.get("summary", "")[:600].strip(),
                    "link": entry.get("link", ""),
                    "published": published.strftime("%d/%m/%Y") if published else "N/A",
                })
        except Exception as exc:
            print(f"[WARN] {source_name}: {exc}")

    print(f"[INFO] Total artículos de la semana: {len(articles)}")
    return articles[:40]


def generate_newsletter_html(articles: list[dict]) -> str:
    client = anthropic.Anthropic()

    articles_text = "\n\n".join(
        f"[{a['source']} - {a['published']}]\nTítulo: {a['title']}\nResumen: {a['summary']}\nURL: {a['link']}"
        for a in articles
    )
    week_range = (
        f"{(datetime.now() - timedelta(days=6)).strftime('%d/%m/%Y')} "
        f"– {datetime.now().strftime('%d/%m/%Y')}"
    )

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
- HTML completo con estilos CSS inline (compatible con clientes de email).
- Diseño oscuro y profesional: fondo #0f0f1a, texto claro, acentos en #6366f1 (índigo).
- Estructura obligatoria:
  1. Header con "🤖 AI Weekly" y la fecha de la semana
  2. "Resumen Ejecutivo" – 4-5 bullet points clave
  3. "Google & DeepMind" – sus noticias
  4. "Anthropic" – sus noticias
  5. "OpenAI" – sus noticias
  6. "Tendencias Empresariales" – adopción de IA en empresas
  7. "Nuevos Modelos & Productos" – lanzamientos de la semana
  8. "Para Tener en el Radar" – tendencias emergentes
  9. Footer con "Generado con Claude Sonnet" y la fecha
- Cada noticia con enlace clickeable al artículo original.
- Si no hay noticias de una sección: "Sin novedades esta semana."
- Solo HTML y CSS inline, sin JavaScript.""",
        }],
    )

    html = response.content[0].text
    print(f"[INFO] HTML generado: {len(html)} caracteres")
    return html


def send_email(html_body: str) -> None:
    gmail_user = os.environ["GMAIL_USER"]
    gmail_password = os.environ["GMAIL_APP_PASSWORD"]
    recipient = os.environ["RECIPIENT_EMAIL"]

    print(f"[INFO] Enviando email a {recipient}...")
    subject = f"🤖 AI Weekly · Resumen IA empresarial · semana del {datetime.now().strftime('%d/%m/%Y')}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"AI Weekly Newsletter <{gmail_user}>"
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient, msg.as_string())

    print(f"[OK] Newsletter enviado a {recipient}")


def main() -> None:
    print("[START] Generando newsletter semanal de IA...")

    try:
        articles = fetch_week_articles()
    except Exception:
        print("[ERROR] fetch_week_articles:")
        traceback.print_exc()
        raise

    if not articles:
        print("[WARN] Sin artículos esta semana, usando placeholder...")
        articles = [{"source": "Aviso", "title": "Sin noticias recopiladas esta semana",
                     "summary": "", "link": "", "published": "N/A"}]

    try:
        html = generate_newsletter_html(articles)
    except Exception:
        print("[ERROR] generate_newsletter_html:")
        traceback.print_exc()
        raise

    try:
        send_email(html)
    except Exception:
        print("[ERROR] send_email:")
        traceback.print_exc()
        raise

    print("[DONE] Completado exitosamente.")


if __name__ == "__main__":
    main()
