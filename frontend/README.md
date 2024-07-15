# Frontend SPA

This is a single-page application (SPA) built with Vue.js
designed to help business owners showcase their businesses
online and for customers to find and read more about
businesses and their products.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Node.js (version v22.2.0)
- npm (version 10.7.0)

**NOTE:** We use Auth0 for authentication.
Make sure you have an account up and running.

### Installing
```bash
# Clone the repository
git clone https://github.com/10thcode/business.git

# Navigate into the project directory
cd business/frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Features
- Business Owners can showcase their businesses
- Customers can browse and read about businesses
- Intuitive UI
- Optimized for mobile

## Configuration
```bash
# .env
VITE_API_URL=your_api_url
VITE_AUTH0_DOMAIN=your_auth0_domain
VITE_AUTH0_CLIENT_ID=your_auth0_client_id
```

## Scripts
```bash
# Start the development server
npm run dev

# Build the project for production
npm run build
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.
