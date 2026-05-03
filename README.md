# Claude Skills — Julio Flores

Skills personales para Claude Code. Se instalan en `~/.claude/skills/`.

---

## Newsletter Semanal de IA

Automatización que envía cada **domingo a las 20:00h (hora España)** un email con el resumen de las noticias más importantes de la semana sobre IA empresarial: Google, Anthropic, OpenAI y tendencias del sector.

### Cómo funciona

1. GitHub Actions ejecuta el script cada domingo a las 18:00 UTC (= 20:00 CEST)
2. Se recopilan artículos de 8 fuentes RSS (Google AI, OpenAI, Anthropic, MIT Tech Review, VentureBeat, TechCrunch, The Verge, Ars Technica)
3. Claude Sonnet genera un newsletter HTML en español con diseño profesional
4. El email se envía vía Gmail SMTP al destinatario configurado

### Configuración: GitHub Secrets requeridos

Ve a **Settings → Secrets and variables → Actions** en tu repositorio y añade:

| Secret | Descripción |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Tu API key de Anthropic (console.anthropic.com) |
| `GMAIL_USER` | Tu cuenta de Gmail (ej: tunombre@gmail.com) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Gmail (no la normal) |
| `RECIPIENT_EMAIL` | Email donde recibirás el newsletter |

> **Cómo obtener la contraseña de aplicación de Gmail:**
> Google Account → Seguridad → Verificación en dos pasos → Contraseñas de aplicaciones → Crear

### Ejecución manual

Puedes lanzar el newsletter en cualquier momento desde **Actions → Weekly AI Newsletter → Run workflow**.

---

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

## Instalación de skills

```bash
# Mac/Linux
cp *.skill ~/.claude/skills/

# Windows (PowerShell)
Copy-Item "*.skill" "$env:USERPROFILE\.claude\skills\"
```

---

> **Aviso legal**: las skills son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
