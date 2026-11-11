# VM per la lezione 5: come è stata costruita

Documento riservato al docente. Registra la VM preparata l'11–12 novembre 2026 sul PC del docente, con VMware Workstation 17.6.1. La VM sta su `F:\VM_Studenti\ITSMAKER-Win11-Studio\` (disco esterno), fuori dal repository.

## Specifiche

Ricavate dalle foto di Gestione attività di un PC della scuola: Intel Core i7-13700 (16 core, 24 thread), 15,6 GB di RAM (6,9 GB già in uso da fermo), disco NVMe, Intel UHD 770 e NVIDIA T400 da 4 GB, virtualizzazione attiva.

| Voce | Scelta |
| --- | --- |
| Processori virtuali | 4 |
| RAM | 6144 MB (decisione del 12 novembre; era 8192 MB) |
| Scheda grafica | nessuna (la T400 non viene usata) |
| Disco | 64 GB che crescono; usati circa 23 GB |
| Rete | NAT |
| Avvio | UEFI, Secure Boot spento, niente TPM; hardware virtuale versione 20 (VMware 17 o successivo) |
| Windows | 11 Pro 10.0.26300, italiano, non attivato (chiave generica di installazione) |
| Utente | `studente`, password `studente`, amministratore, accesso automatico |
| Nome macchina | `ITS-STUDIO` (uguale in tutte le copie) |

## Contenuto

- Unsloth Studio 2026.11.4, solo CPU, senza PyTorch (`UNSLOTH_NO_TORCH=1`). Nessuna password impostata: la sceglie chi lo apre la prima volta.
- opencode v2.2.7, versione da riga di comando, nel PATH dell'utente `studente`. Non collegato a nessun modello.
- Modello `unsloth/Qwen3.5-2B-GGUF`, file `Qwen3.5-2B-UD-Q4_K_XL.gguf` (1.339.752.704 byte), nella cache di Hugging Face dell'utente. SHA256 uguale a quello pubblicato: `0af96165ea615bea39a04118d63f0b6d35908aea850ee4a51aa6151d851b8b35`.
- VMware Tools.

## Che cosa è stato provato

Con 8192 MB di RAM, nella VM: `llama-server` carica il modello e risponde in italiano a una domanda breve (8 parole in 0,4 secondi, processo da 1,8 GB, 3,4 GB di RAM libera). Studio parte e la pagina su `127.0.0.1:8888` risponde.

## Che cosa non è stato provato

- La VM con 6144 MB di RAM.
- La scheda «On Device» di Studio, Context Length, System Prompt, parametri, base di conoscenza.
- opencode avviato da una nuova finestra.
- La memoria del PC reale con la VM accesa e il browser aperto. Da fermo il PC della scuola usa già 6,9 GB su 15,6.
- La copia su più PC e la domanda «spostata o copiata» alla prima accensione.

## Problema incontrato: libreria Visual C++ vecchia

`llama-server.exe` andava in crash (codice 0xC0000005, modulo `MSVCP140.dll` 14.36.32532 in System32) con qualsiasi comando, anche `--version`. L'immagine Windows 11 usata porta quella versione. Risolto installando il pacchetto ridistribuibile Microsoft Visual C++ aggiornato (`https://aka.ms/vs/17/release/vc_redist.x64.exe`, versione 14.44.35211); l'installazione richiede l'autorizzazione di Windows (finestra del controllo account utente). Su un PC o una VM con Windows 11 da zero lo stesso crash può ripresentarsi.

## Come è stata creata

1. ISO di Windows 11 in italiano (build 26300) con un file `autounattend.xml` per l'installazione senza domande: salta i controlli su TPM, Secure Boot, RAM e processore; edizione Pro; utente locale; fuso orario italiano; installazione di VMware Tools al primo accesso.
2. Per evitare il messaggio «Premi un tasto per avviare da CD», l'ISO è stata ricostruita con il file di avvio `efisys_noprompt.bin` (IMAPI di Windows, solo UDF). L'ISO ricostruita è stata cancellata a fine lavoro; l'originale non è stato toccato.
3. Dentro la VM: `$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex`; opencode da `opencode-windows-x64-baseline.zip` (sito ufficiale) in `%LOCALAPPDATA%\Programs\opencode`; modello con `huggingface_hub` e `HF_HUB_DISABLE_XET=1` (come nelle note su Studio).
