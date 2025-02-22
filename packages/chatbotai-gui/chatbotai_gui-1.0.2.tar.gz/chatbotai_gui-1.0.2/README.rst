ChatbotAI-GUI
=============

**ChatbotAI-GUI** is a graphical user interface (GUI) chatbot that integrates multiple AI models, including OpenAI, Meta AI, and Google Generative AI. This package allows users to interact with different AI models seamlessly through a single application.

✨ Features
------------
- Supports **OpenAI**, **Meta AI API**, and **Google Generative AI**.
- Simple and intuitive GUI for easy interaction.
- Extensible and customizable for different chatbot implementations.

📦 Installation
----------------
Install the package using:

.. code-block:: sh

    pip install chatbotai-gui

🚀 Usage
---------
After installation, you can launch the chatbot GUI using:

.. code-block:: sh

    python -m chatai

Or in a Python script:

.. code-block:: python

    from chatai.chatbotgui import ChatbotApp

    app = ChatbotApp()
    app.run()

📝 Configuration
----------------
The chatbot configuration is stored in `config.json` inside the `chatai` module. You can modify it to adjust settings such as API keys and model preferences.

📜 License
-----------
This project is licensed under the **AGPL-3.0-or-later**. See the `LICENSE` file for more details.
