
**Restaurant Name and Menu Generator**

This project utilizes Hugging Face's language model API through LangChain to generate restaurant names and menu items based on selected cuisines. It offers a streamlined way to brainstorm creative restaurant names and diverse menu items for various cuisines.

### Features

- **Dynamic Selection:** Choose from a variety of cuisines including Italian, French, Chinese, etc.
- **Name Generation:** Automatically generates unique restaurant names tailored to the selected cuisine.
- **Menu Item Generation:** Generates a list of menu items appropriate for the chosen restaurant name.
- **Streamlit Integration:** Uses Streamlit for a user-friendly interface to interact with the model.

### Installation

To run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/restaurant-name-generator.git
   cd restaurant-name-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Hugging Face API key:
   - Obtain your Hugging Face API key and place it in `secret_key.py` as `huggingface_api = "YOUR_API_KEY"`.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

### Usage

- Select a cuisine from the sidebar.
- The application will generate a restaurant name and suggest menu items based on your selection.
- Explore different cuisines and discover unique restaurant concepts!

### Technologies Used

- Python
- Streamlit
- LangChain
- Hugging Face Transformers

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For questions or feedback, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).

---

Adjust the URLs, email address, and specific details to match your project. This structure should help users understand what your project does, how to use it, and how they can contribute.
