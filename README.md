# Claude Skills — Julio Flores

Skills personales para Claude Code. Se instalan en `~/.claude/skills/`.

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

## Automatizaciones

### 🤖 Newsletter Semanal de IA ([`weekly_ai_newsletter.py`](./weekly_ai_newsletter.py))

Cada **domingo a las 20:00 h** (hora España, verano) recibes un correo HTML con el resumen ejecutivo de la semana en inteligencia artificial.

**Fuentes monitorizadas:**
- Google AI Blog, OpenAI Blog, Anthropic News
- MIT Technology Review, VentureBeat AI, TechCrunch AI, The Verge, Ars Technica

**Contenido del email:**
1. Resumen ejecutivo (bullet points clave)
2. Noticias de Google & DeepMind
3. Noticias de Anthropic
4. Noticias de OpenAI
5. Tendencias empresariales de IA
6. Nuevos modelos y productos lanzados
7. Cosas a tener en el radar

**Tecnología:** Python + RSS feeds + Claude Sonnet (resumen con IA) + Gmail SMTP.

#### Configuración (una sola vez)

Ve a tu repositorio en GitHub → **Settings → Secrets and variables → Actions** y añade estos 4 secrets:

| Secret | Valor |
|--------|-------|
| `ANTHROPIC_API_KEY` | Tu clave de API de Anthropic (console.anthropic.com) |
| `GMAIL_USER` | Tu dirección de Gmail (ej: tunombre@gmail.com) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Gmail (no tu contraseña normal) |
| `RECIPIENT_EMAIL` | Email donde quieres recibir el newsletter |

> **Cómo obtener la contraseña de aplicación de Gmail:**
> Google Account → Seguridad → Verificación en dos pasos (activada) → Contraseñas de aplicaciones → Crear una nueva.

#### Horario

El workflow de GitHub Actions usa UTC. El cron está configurado a `0 18 * * 0` (domingo 18:00 UTC):
- **Verano (CEST = UTC+2):** 20:00 h España ✅
- **Invierno (CET = UTC+1):** 19:00 h España (una hora antes)

#### Ejecución manual

Puedes lanzarlo en cualquier momento desde GitHub → **Actions → Weekly AI Newsletter → Run workflow**.

---

## Instalación de Skills

### Instalar todas las skills

```bash
# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"

# Mac/Linux
cp *.skill ~/.claude/skills/
```

### Instalar una skill concreta

```bash
# Windows
Copy-Item "web-security-audit.skill" "$env:USERPROFILE\.claude\skills\"

# Mac/Linux
cp web-security-audit.skill ~/.claude/skills/
```

## Uso de las skills

Una vez instalada, escribe en Claude Code:

```
hazme una auditoría de seguridad de https://miweb.com
```

Claude pedirá confirmación de autorización antes de ejecutar ningún test.

---

> **Aviso legal**: estas skills son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
