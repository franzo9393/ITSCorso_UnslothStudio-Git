# Prepara la macchina virtuale per la lezione 5. Si esegue una volta sola, dentro la VM.
#
# Mettete in una cartella (per esempio una cartella condivisa con VMware o una chiavetta) questo file
# e i quattro file della cartella di lavoro: inventario.csv, appunti_riunione.txt e da_fare.txt
# (da docente/CARTELLA_LABORATORIO/) e opencode.jsonc (da docente/MODELLI_OPENCODE/).
# Poi, dentro la VM, aprite PowerShell in quella cartella e scrivete:
#
#     powershell -ExecutionPolicy Bypass -File .\PREPARA_VM_LEZIONE5.ps1
#
# Lo script crea la cartella Documenti\laboratorio con i quattro file e mette sul desktop
# il collegamento "opencode", che avvia opencode in quella cartella.
# Se esiste la vecchia cartella Documenti\noleggio (versione precedente della lezione),
# toglie i quattro file che la preparazione vi aveva messo e la cancella se resta vuota.
# Non modifica Unsloth Studio e non tocca altro nella VM. Si puo' rilanciare senza danni.
#
# Con -Pulisci (usato dalla VM preparata offline) alla fine cancella da Public\Documents i file di
# partenza, il richiamo nella cartella Esecuzione automatica e se stesso.

param(
    [string]$Origine = $PSScriptRoot,
    [switch]$Pulisci
)
$ErrorActionPreference = 'Stop'

$file = @(
    'inventario.csv',
    'appunti_riunione.txt',
    'da_fare.txt',
    'opencode.jsonc'
)

foreach ($nome in $file) {
    if (-not (Test-Path -LiteralPath (Join-Path $Origine $nome))) {
        throw "Manca il file $nome in $Origine"
    }
}

$documenti = [Environment]::GetFolderPath('MyDocuments')

# Versione precedente della lezione: cartella noleggio con i tre testi e opencode.jsonc.
$vecchia = Join-Path $documenti 'noleggio'
if (Test-Path -LiteralPath $vecchia) {
    foreach ($nome in @(
        'Registro_Ruota_Libera_7-8_novembre_2026.txt',
        'Regole_noleggio_Ruota_Libera.txt',
        'Guida_guasti_Ruota_Libera.txt',
        'opencode.jsonc'
    )) {
        Remove-Item -LiteralPath (Join-Path $vecchia $nome) -Force -ErrorAction SilentlyContinue
    }
    if (-not (Get-ChildItem -LiteralPath $vecchia -Force)) {
        Remove-Item -LiteralPath $vecchia -Force
    } else {
        Write-Host "Attenzione: nella vecchia cartella $vecchia restano altri file, non cancellati."
    }
}

$cartella = Join-Path $documenti 'laboratorio'
New-Item -ItemType Directory -Force -Path $cartella | Out-Null
foreach ($nome in $file) {
    Copy-Item -LiteralPath (Join-Path $Origine $nome) -Destination $cartella -Force
}

$collegamento = Join-Path ([Environment]::GetFolderPath('Desktop')) 'opencode.lnk'
$shell = New-Object -ComObject WScript.Shell
$link = $shell.CreateShortcut($collegamento)
$link.TargetPath = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$link.Arguments = '-NoExit -Command "opencode"'
$link.WorkingDirectory = $cartella
$link.Description = 'Avvia opencode nella cartella laboratorio'
$link.Save()

Write-Host "Fatto. Cartella: $cartella"
Write-Host "Collegamento: $collegamento"
Get-ChildItem -LiteralPath $cartella | Select-Object Name, Length

if ($Pulisci) {
    foreach ($nome in $file) {
        Remove-Item -LiteralPath (Join-Path $Origine $nome) -Force -ErrorAction SilentlyContinue
    }
    $avvio = Join-Path $env:ProgramData 'Microsoft\Windows\Start Menu\Programs\Startup\prepara_lezione5.cmd'
    Remove-Item -LiteralPath $avvio -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $PSCommandPath -Force -ErrorAction SilentlyContinue
}
