# AGENTS.md

Flask-kirjautumissovellus, jota testataan Robot Frameworkilla (Browser-kirjasto).

## Komennot

Projekti on uv-projekti. Suorita kaikki komennot projektin juuresta muodossa `uv run ...`.

- Riippuvuuksien asennus: `uv sync`
- Sovelluksen käynnistys: `uv run python src/index.py` (osoite http://localhost:5001, debug-tila lataa koodimuutokset automaattisesti)
- Testit: `uv run robot src/tests`
- Yksi testitiedosto: `uv run robot src/tests/login.robot`
- Ilman selainikkunaa: `uv run robot --variable HEADLESS:true src/tests`

Sovelluksen on oltava käynnissä portissa 5001 testien aikana. Testit eivät käynnistä sitä itse.

## Rakenne

- `src/index.py`: käynnistys, `src/app.py`: Flask-reitit
- `src/services/user_service.py`: sovelluslogiikka. Käyttäjätunnuksen ja salasanan validointi tapahtuu `UserService`-luokan metodissa `validate`, joka nostaa `UserInputError`-virheen. Virheen teksti näytetään käyttäjälle sellaisenaan.
- `src/repositories/user_repository.py`: käyttäjät muistissa, ei tietokantaa
- `src/templates/`: sivupohjat
- `src/tests/*.robot`: testit, `src/tests/resource.robot`: yhteiset avainsanat ja muuttujat
- `src/AppLibrary.py`: testien Python-avainsanat (`Reset Application`, `Create User`)

## Testeistä

- Testit tunnistavat sivut `<title>`-otsikosta ja virheet ilmoitustekstistä. Jos muutat otsikkoa tai virheilmoitusta, päivitä myös testit.
- `Create User` tekee POST-pyynnön osoitteeseen `/register`, joten testien luomat käyttäjät kulkevat saman validoinnin läpi.
- `POST /tests/reset` tyhjentää käyttäjät testien välillä.
