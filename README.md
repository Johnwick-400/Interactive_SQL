# Interactive SQL (Upload, Prompt, Analyse)

Welcome to Interactive SQL! This project aims to simplify the process of analyzing datasets using SQL queries. Users can upload their datasets in CSV format, input their desired SQL prompt, and our API will generate the query and display the output accordingly.

## Getting Started

To get started with Interactive SQL, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Johnwick-400/Interactive_SQL
   cd Interactive_SQL
   ```

2. **Install the Requirements**
  ```bash
   pip install -r requirements.txt
   ```
   
3. **Get Your Gemini API Key**
   You'll need to obtain your Gemini API key and paste it into the code to enable the functionality.

4. **Run the Application**
   ```bash
   streamlit run sql.py
   ```
   This command will start the Streamlit application and launch the Interactive SQL interface in your browser.

## Usage

1. **Upload Dataset**
   - Click on the "Upload" button to select and upload your dataset in CSV format.

2. **Input SQL Prompt**
   - Below the uploaded dataset, enter your SQL prompt/query.

3. **Generate and Analyse**
   - Once you've entered your prompt, our API will generate the corresponding SQL query and display the output based on your requirements.

## Example

Here's an example of how to use Interactive SQL:

1. Upload a dataset named `example_data.csv`.
2. Input the SQL prompt: `SHOW THE DATA;`
3. Click on "Generate Query" to see the filtered results.

## Support and Feedback

If you encounter any issues or have suggestions for improvement, please feel free to open an issue or reach out to us. Your feedback is valuable in enhancing the functionality and usability of Interactive SQL.

Happy querying! 🚀
