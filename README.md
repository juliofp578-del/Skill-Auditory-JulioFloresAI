# Claude Skills — Julio Flores

Skills personales para Claude Code y automatizaciones con IA.

---

## 🤖 Newsletter Semanal de IA Empresarial

Cada **domingo a las 20:00 h** (hora España, verano) recibirás un email con el resumen de la semana en IA empresarial: Google/DeepMind, Anthropic, OpenAI, tendencias, nuevos modelos y más.

### Cómo funciona

1. **GitHub Actions** lanza el workflow cada domingo (`cron: '0 18 * * 0'` UTC = 20:00 CEST)
2. El script Python recoge artículos de los últimos 7 días desde 8 fuentes RSS (Google AI Blog, OpenAI, Anthropic, MIT Tech Review, VentureBeat, TechCrunch, The Verge, Ars Technica)
3. **Claude Sonnet** genera un newsletter HTML con diseño profesional en español
4. Se envía por email vía Gmail SMTP

### Configuración (única vez)

Necesitas configurar **4 GitHub Secrets** en el repositorio:

`Settings → Secrets and variables → Actions → New repository secret`

| Secret | Qué poner |
|--------|-----------|
| `ANTHROPIC_API_KEY` | Tu API Key de [console.anthropic.com](https://console.anthropic.com) |
| `GMAIL_USER` | Tu dirección de Gmail, ej: `tumail@gmail.com` |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Google (no tu contraseña normal) |
| `RECIPIENT_EMAIL` | Email donde quieres recibir el newsletter |

#### Cómo generar la contraseña de aplicación de Google

1. Ve a [myaccount.google.com/security](https://myaccount.google.com/security)
2. Activa la **verificación en 2 pasos** (si no la tienes)
3. Busca **"Contraseñas de aplicaciones"**
4. Crea una nueva para "Correo / Otro" → copia los 16 caracteres

### Probar manualmente

En GitHub: `Actions → 🤖 Weekly AI Newsletter → Run workflow`

### Archivos

| Archivo | Descripción |
|---------|-------------|
| `weekly_ai_newsletter.py` | Script principal (fetch RSS → Claude → Gmail) |
| `.github/workflows/weekly-ai-newsletter.yml` | Workflow de GitHub Actions |
| `requirements.txt` | Dependencias Python (`anthropic`, `feedparser`) |

---

## Skills para Claude Code

Se instalan en `~/.claude/skills/`.

| Skill | Descripción | Activación |
|-------|-------------|------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

### Instalación

```bash
# Mac/Linux
cp *.skill ~/.claude/skills/

# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"
```

---

> **Aviso legal**: las skills de auditoría son para uso en sistemas propios o con autorización explícita del propietario.
