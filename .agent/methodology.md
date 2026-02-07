# Project Methodology: Villa Kunterbunt

This document outlines the hierarchy and metadata standards for the different project branches.

## 1. Project Branches

The project is divided into three main levels of depth:

| Branch | Technical Path | Description | Page Title (Example) |
| :--- | :--- | :--- | :--- |
| **Main** | `core/data/main/` | **Die Villa Kunterbunt - Korrespondenz Epos** | Das Epos |
| **Cowork** | `core/data/cowork/` | **Die Villa Kunterbunt - Anthologie & Apokryphen** | Die Anthologie |
| **Meta** | `core/data/meta/` | **Die Villa Kunterbunt - das Kompendium** | Das Kompendium |

## 2. Meta Section Naming (Kompendium)

Episodes in the `meta` section follow a specific "Study/Analysis" naming convention:

- **Episode 1 Tag**: `E01: Die erweiterte Studienanalyse`
- **Episode 1 Title**: `Die erweiterte Studienanalyse`
- **URL**: `core/data/meta/podcast/korrespondenz_system_analyse.html`

## 3. MediaSession & Widget Metadata (iPhone)

To ensure high-quality display on iPhone widgets and lock screens, use the following mapping:

- **Metadata Title**: Match the specific episode title (e.g., `E01: Die erweiterte Studienanalyse`).
- **Metadata Album**: Include the full project level name (e.g., `Das Villa Kunterbunt Kompendium`).
- **Metadata Artist**: `Die Villa Kunterbunt`.
- **Artwork**: 
    - Front Cover from: `/meta/images/*abook*front*.png`
    - Back Cover from: `/meta/images/*abook*back*.png`
    - (Stored as thumbs in `/meta/images/thumbs/`)

## 4. Directory Conventions

- `podcast/index.html`: Main landing page for a section.
- `podcast/.queue/`: For auxiliary episodes (non-featured).
- `audio/.queue/`: For corresponding audio files.
