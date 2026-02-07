# Project Structure: Podcast Directory

This document records the reorganized structure of the podcast and audio directories as of February 2026.

## 1. Web Pages (`core/data/main/podcast/`)

The directory has been cleaned up to focus on the landing page and the audiobook.

- **index.html**: Main landing page. Features only the Audiobook (Episode 01) to provide a focused entry point.
- **abook.html**: Dedicated page for the Audiobook (Episode 01).
- **.queue/**: Subdirectory containing individual pages for all other episodes (02–08).
    - `satire.html` (Episode 02)
    - `analyse.html` (Episode 03)
    - `dossier.html` (Episode 04)
    - `deepdive.html` (Episode 05)
    - `zupftest.html` (Episode 06)
    - `systemanalyse.html` (Episode 07)
    - `korrespondenz_epos.html` (Episode 08)

## 2. Audio Files (`core/data/main/audio/`)

Audio files are organized to match the page structure.

- **Die Villa Kunterbunt - Das Hörbuch.mp3**: Main audiobook file.
- **.queue/**: Subdirectory containing MP3 files for the podcast episodes.
    - `villa_kunterbunt_satire_podcast.mp3`
    - `villa_kunterbunt_analyse_podcast.mp3`
    - `villa_kunterbunt_dossier_podcast.mp3`
    - `villa_kunterbunt_deepdive_podcast.mp3`
    - `villa_kunterbunt_zupftest_podcast.mp3`
    - `villa_kunterbunt_die_studie_podcast.mp3`
    - `villa_kunterbunt_korrespondenz_epos.mp3`

## 3. Navigation Logic

Episodes are linked sequentially (01–08). Navigation links on the detail pages handle cross-directory transitions between the top-level `abook.html` and the files in `.queue/`.
