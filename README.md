# Claude Skills — Julio Flores

Skills personales para Claude Code y automatizaciones con IA.

---

## 🤖 Newsletter Semanal de IA Empresarial

**Envío automático cada domingo a las 20:00 h (hora España)** con un resumen ejecutivo de las noticias más relevantes de la semana sobre IA, Google, Anthropic, OpenAI y adopción empresarial.

### ¿Cómo funciona?

1. **GitHub Actions** dispara el workflow cada domingo a las 18:00 UTC (20:00 CEST)
2. El script Python **recopila artículos** de 8 fuentes RSS (Google AI, OpenAI, Anthropic, MIT Tech Review, VentureBeat, TechCrunch, The Verge, Ars Technica)
3. **Claude Sonnet** genera un newsletter HTML con diseño profesional y resumen ejecutivo en español
4. Se envía a tu correo vía **Gmail SMTP**

### Configuración (solo una vez)

Ve a **Settings → Secrets and variables → Actions** en este repositorio y añade estos 4 secrets:

| Secret | Valor |
|--------|-------|
| `ANTHROPIC_API_KEY` | Tu API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com)) |
| `GMAIL_USER` | Tu cuenta Gmail (ej. `tunombre@gmail.com`) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación Gmail ([ver instrucciones](#contraseña-de-aplicación-gmail)) |
| `RECIPIENT_EMAIL` | Email destino donde recibirás el newsletter |

#### Contraseña de aplicación Gmail

1. Activa la **verificación en 2 pasos** en tu cuenta Google
2. Ve a [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Crea una nueva app password con nombre "AI Newsletter"
4. Copia la contraseña generada (16 caracteres) como `GMAIL_APP_PASSWORD`

### Ejecución manual

Una vez configurados los secrets, puedes lanzar el newsletter en cualquier momento desde:
**Actions → 🤖 Weekly AI Newsletter → Run workflow**

### Estructura del newsletter

Cada domingo recibirás un email HTML con:
- **Resumen Ejecutivo** — 4-5 puntos clave de la semana
- **Google & DeepMind** — novedades de sus equipos de IA
- **Anthropic** — actualizaciones de Claude y la empresa
- **OpenAI** — lanzamientos y noticias de la semana
- **Tendencias Empresariales** — adopción de IA en negocios
- **Nuevos Modelos & Productos** — lanzamientos destacados
- **Para Tener en el Radar** — tendencias emergentes

---

## Skills disponibles

| Skill | Descripción | Activación |
|-------|-------------|------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

## Instalación de skills

```bash
# Mac/Linux
cp *.skill ~/.claude/skills/

# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"
```

---

> **Aviso legal**: las skills de auditoría son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
