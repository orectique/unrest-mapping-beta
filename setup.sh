mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base=\"light\"\n\
primaryColor=\"#778da9\"\n\
font=\"sans serif\"\n\
" > ~/.streamlit/config.toml