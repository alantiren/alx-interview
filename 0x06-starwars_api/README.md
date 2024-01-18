# Star Wars Characters Script

## Overview

This project includes a script written in JavaScript that interacts with the Star Wars API to retrieve and display the characters of a specific Star Wars movie. The script takes the Movie ID as a command-line argument and makes API requests to fetch and display the characters.

## Project Structure

- **File**: `0-starwars_characters.js`
  - The main script file containing the logic for fetching and displaying Star Wars characters.

## Prerequisites

- Node.js 10 installed. You can install it using the following commands:
  ```bash
  curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  sudo apt-get install -y nodejs
  ```

- Semi-standard coding style is used. Install it globally with:
  ```bash
  sudo npm install semistandard --global
  ```

- Request module is required. Install it globally with:
  ```bash
  sudo npm install request --global
  export NODE_PATH=/usr/lib/node_modules
  ```

## How to Run

To execute the script, use the following command in the terminal:

```bash
./0-starwars_characters.js <Movie ID>
```

Replace `<Movie ID>` with the ID of the Star Wars movie you want to retrieve characters from.

## Example

```bash
./0-starwars_characters.js 3
```

Output:
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Notes

- All files must end with a new line.
- The first line of all files must be exactly `#!/usr/bin/node`.
- The script follows the Semi-standard coding style, including semicolons.
- Ensure that all files are executable.

## Author

- **Alexa Orrico** - Software Engineer at Holberton School
