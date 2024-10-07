# Mumbai IT Solutions

![Banner](images/banner.png)

Welcome to **Mumbai IT Solutions**, your go-to Discord bot for all things tech-related... or not! We provide questionable support and hilarious responses to your tech troubles.

## Prerequisites

To run this bot, you need to have **Docker** installed on your machine. You can download Docker from the official website: [Docker](https://www.docker.com/).

## Docker Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmedallion/Mumbai-IT-Solutions.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mumbai-it-solutions
   ```

3. Build the Docker image:
   ```bash
   docker build -t mumbai-it-solutions:1.0.0 .
   ```

4. Run the Docker container in detached mode:
   ```bash
   docker run -d --restart unless-stopped --name mumbai-it-solutions -h mumbai-it-solutions -e BOT_TOKEN=your_bot_token_here mumbai-it-solutions:1.0.0
   ```

## Usage

- To stop the bot running in the Docker container, use:

    ```bash
    docker stop mumbai-it-solutions
    ```

- To start the bot running in the Docker container, use:

    ```bash
    docker start mumbai-it-solutions
    ```

    Replace `mumbai-it-solutions` with the name or ID of your running container.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

![Logo](images/logo.png)

## Images

All images in this project were created using the [OpenAI's DALL·E](https://openai.com/index/dall-e/).

## Disclaimer

This is not a real company. Just a fun Discord bot! Enjoy the humor and stay safe online!