# Configuración de Git

## Estado del Repositorio

El repositorio Git ha sido inicializado exitosamente en:
```
C:\Users\shpctac1003e\Desktop\30-archivos
```

### Información del Repositorio
- **Rama**: master
- **Commit inicial**: 362644e - "Initial commit: 30 Python exercises with solutions"
- **Archivos**: 33 archivos (30 ejercicios Python + documentación)

## Cómo usar Git

### Opción 1: Usar el script git.bat (Recomendado)
```batch
cd C:\Users\shpctac1003e\Desktop\30-archivos
git.bat status
git.bat log
git.bat add .
git.bat commit -m "tu mensaje"
```

### Opción 2: Usar PowerShell (Con ruta completa)
```powershell
$env:GIT_PATH = "C:\Users\shpctac1003e\AppData\Local\Temp\PortableGit\bin\git.exe"
cd "C:\Users\shpctac1003e\Desktop\30-archivos"
& $env:GIT_PATH status
& $env:GIT_PATH log
& $env:GIT_PATH add .
& $env:GIT_PATH commit -m "tu mensaje"
```

### Opción 3: Instalar Git globalmente (Opcional)
Si deseas usar Git desde cualquier carpeta, puedes instalar Git for Windows desde:
https://git-scm.com/download/win

## Comandos Git Útiles

### Ver estado del repositorio
```bash
git status
```

### Ver el registro de commits
```bash
git log
```

### Ver cambios sin comprometer
```bash
git diff
```

### Añadir cambios
```bash
git add .
```

### Hacer commit
```bash
git commit -m "Descripción de los cambios"
```

### Ver cambios en un archivo específico
```bash
git diff ejercicio_01.py
```

## Detalles de la Instalación

Se instaló **Git Portable v2.45.0** en:
- **Ubicación**: `C:\Users\shpctac1003e\AppData\Local\Temp\PortableGit`
- **Ventaja**: No requiere instalación global del sistema
- **Desventaja**: Solo funciona desde esta carpeta o si añades la ruta a PATH

## Próximos Pasos

1. **Para clonar este repositorio** en otra ubicación:
   ```bash
   git clone C:\Users\shpctac1003e\Desktop\30-archivos Nueva-Carpeta
   ```

2. **Para conectar con GitHub** (si deseas):
   - Crea una cuenta en https://github.com
   - Crea un repositorio vacío en GitHub
   - Ejecuta:
   ```bash
   git remote add origin https://github.com/tu-usuario/tu-repo.git
   git push -u origin master
   ```

3. **Para actualizar cambios en el repositorio**:
   ```bash
   git add .
   git commit -m "Descripción de cambios"
   git push origin master  # (Si está conectado a GitHub)
   ```

## Notas Importantes

- ✅ Git está configurado localmente con usuario: "Usuario"
- ✅ Email configurado: "usuario@example.com"
- ✅ Todos los 30 ejercicios están en el repositorio
- ✅ Se incluyó documentación (.gitignore, README.md, GUIA_DE_USO.md)
- ⚠️ Git Portable está en la carpeta TEMP - puede eliminarse al reiniciar (crear permanente si es necesario)

## Crear Instalación Permanente de Git

Si deseas que Git sea permanente, mueve la carpeta PortableGit:

```powershell
Move-Item "C:\Users\shpctac1003e\AppData\Local\Temp\PortableGit" "C:\Program Files\PortableGit"
```

Luego actualiza la ruta en git.bat a:
```batch
set PATH=C:\Program Files\PortableGit\bin;%PATH%
```
