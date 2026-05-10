# Claude Skills — Julio Flores

Skills personales para Claude Code. Se instalan en `~/.claude/skills/`.

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

---

## 🤖 Newsletter Semanal de IA Empresarial

Automatización que envía cada **domingo a las 20:00 h** (hora Madrid, verano) un email con el resumen semanal de noticias de IA empresarial: Google, Anthropic, OpenAI y tendencias del sector.

### Cómo funciona

1. GitHub Actions ejecuta el workflow cada domingo a las 18:00 UTC (20:00 Madrid en verano, 19:00 en invierno).
2. El script Python descarga artículos de 8 feeds RSS de los principales medios de IA.
3. Claude Sonnet genera un newsletter HTML profesional en español.
4. Se envía al correo configurado vía Gmail SMTP.

### Fuentes de noticias

- Google AI Blog
- OpenAI Blog
- Anthropic News
- MIT Technology Review (IA)
- VentureBeat AI
- TechCrunch AI
- The Verge AI
- Ars Technica

### Configuración — GitHub Secrets necesarios

Ve a tu repositorio en GitHub → **Settings → Secrets and variables → Actions → New repository secret** y crea los siguientes 4 secrets:

| Secret | Descripción |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Tu API key de Anthropic (empieza por `sk-ant-...`) |
| `GMAIL_USER` | Tu dirección Gmail completa (ej: `tunombre@gmail.com`) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación Gmail (16 caracteres, **NO** tu contraseña normal) |
| `RECIPIENT_EMAIL` | Correo donde quieres recibir el newsletter |

### Cómo obtener la contraseña de aplicación Gmail

1. Activa la **verificación en 2 pasos** en tu cuenta Google.
2. Ve a [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
3. Crea una nueva contraseña de aplicación → selecciona "Correo" y "Otro (nombre personalizado)" → escribe "AI Newsletter".
4. Copia los 16 caracteres que te genera y úsalos como `GMAIL_APP_PASSWORD`.

### Activar el workflow

El workflow está en `.github/workflows/weekly-ai-newsletter.yml`. Para que las ejecuciones programadas funcionen:

1. Haz **merge de esta rama a `main`** (los scheduled workflows de GitHub Actions solo se ejecutan desde la rama por defecto).
2. Ve a **Actions** en tu repositorio y asegúrate de que el workflow no está desactivado.
3. Para probar manualmente: Actions → "🤖 Weekly AI Newsletter" → **Run workflow**.

### Archivos de la automatización

```
weekly_ai_newsletter.py              # Script principal
.github/workflows/weekly-ai-newsletter.yml  # GitHub Actions
requirements.txt                     # Dependencias Python
```

---

## Instalación de Skills

```bash
# Mac/Linux
cp *.skill ~/.claude/skills/

# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"
```

---

> **Aviso legal**: las skills de auditoría son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
