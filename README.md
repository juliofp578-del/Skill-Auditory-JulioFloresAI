# Claude Skills — Julio Flores

Skills personales para Claude Code. Se instalan en `~/.claude/skills/`.

## Skills disponibles

| Skill | Descripción | Comando de activación |
|-------|-------------|----------------------|
| [web-security-audit](./web-security-audit.skill) | Pentest black-box completo (70+ tests, OWASP Top 10, informe HTML) | *"hazme una auditoría de seguridad de https://..."* |

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
