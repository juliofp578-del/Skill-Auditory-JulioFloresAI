# Claude Skills — Julio Flores

Skills personales para Claude Code. Se instalan en `~/.claude/skills/`.

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

---

## 🤖 Newsletter Semanal de IA

Automatización que cada **domingo a las 20:00 h (hora España)** envía un correo con el resumen de la semana en IA empresarial: Google/DeepMind, Anthropic, OpenAI, tendencias y nuevos modelos.

### Cómo funciona

1. **GitHub Actions** lanza el script cada domingo a las 18:00 UTC (= 20:00 CEST / 19:00 CET).
2. **`weekly_ai_newsletter.py`** recoge artículos de los RSS de Google AI Blog, OpenAI, Anthropic, MIT Tech Review, VentureBeat, TechCrunch, The Verge y Ars Technica.
3. **Claude API** (claude-sonnet-4-6) genera el HTML completo del newsletter con diseño profesional.
4. Se envía al correo configurado vía **Gmail SMTP**.

### Configuración de Secrets (obligatorio)

Ve a tu repositorio → **Settings → Secrets and variables → Actions → New repository secret** y añade los 4 secrets:

| Secret | Valor |
|--------|-------|
| `ANTHROPIC_API_KEY` | Tu API key de Anthropic (https://console.anthropic.com) |
| `GMAIL_USER` | Tu dirección Gmail (ej. `juliofp578@gmail.com`) |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Gmail (ver abajo) |
| `RECIPIENT_EMAIL` | Email donde quieres recibir el newsletter |

#### Cómo obtener la contraseña de aplicación de Gmail

1. Ve a tu cuenta Google → **Seguridad**
2. Activa la **verificación en dos pasos** (necesaria)
3. Busca **"Contraseñas de aplicaciones"**
4. Crea una nueva con nombre "Newsletter IA" → copia los 16 caracteres
5. Usa esos 16 caracteres como valor de `GMAIL_APP_PASSWORD`

### Ejecutar manualmente (para probar)

En tu repositorio → **Actions → 🤖 Weekly AI Newsletter → Run workflow**.

## Instalación

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

## Uso

Una vez instalada, escribe en Claude Code:

```
hazme una auditoría de seguridad de https://miweb.com
```

Claude pedirá confirmación de autorización antes de ejecutar ningún test.

---

> **Aviso legal**: estas skills son para uso en sistemas propios o con autorización explícita del propietario. El uso no autorizado puede ser ilegal.
