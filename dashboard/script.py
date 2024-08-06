import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.graph_objects as go
import plotly.express as px

# Set the page title and icon
st.set_page_config(page_title="Olist E-Commerce Data Analysis Dashboard", page_icon="🛍️")

# Load the dataset
all_df = pd.read_csv('data/all_data.csv')
    
# Define the options for navigation
nav_options = ["Home", "Dataset", "Customer Analysis" , "Geolocation Analysis",
               "Payment Method Analysis", "Review Analysis" , "Order Analysis",
                "Products Analysis",
                "RFM Analysis",]


# Create a sidebar for navigation
st.sidebar.image("assets/sidebar_logo.png", use_column_width=True)
selected_option = st.sidebar.selectbox("Navigate to", nav_options)

# ---------------------------------- Define the content for each page----------------------------------------------------------------

if selected_option == "Home":
    
    # Display the main title
    st.title("Welcome to the Olist E-Commerce Data Analysis Dashboard 📊")
    st.image("assets/home_picture.png")
    # Display subtitles and sections
    st.markdown("##### Discover Insights from Brazil's Leading Marketplace")
    st.write("")
    st.markdown("""
    ### About the Dataset 📚

    Welcome! Explore a comprehensive Brazilian e-commerce public dataset provided by Olist, the largest department store in Brazilian marketplaces. This dataset includes information on 100,000 orders made between 2016 and 2018 across multiple marketplaces in Brazil.
    
    This dataset based on [kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
    """)

    st.write("")
    st.markdown("""
    <style>
    .link-item {
        text-decoration: none;
        color: #FFC857;
        font-weight: bold;
    }
    .link-item:hover {
        color: #FFC857;
    }
    </style>

    ### What You Can Learn 🔎

    Explore the dataset's features to gain valuable insights across various dimensions of an order:

    <ul>
        <li><a class="link-item" href="#Customer_Analysis">Customer Analysis</a>: Understand customer behavior, identify patterns in purchasing, and segment customers based on their interactions with the business.</li>
        <li><a class="link-item" href="#Geolocation_Analysis">Geolocation Analysis</a>: Analyze the geographical distribution of orders to uncover regional trends and optimize delivery strategies.</li>
        <li><a class="link-item" href="#Payment_Method_Analysis">Payment Method Analysis</a>: Examine the different payment methods used by customers, identify preferences, and assess the impact on overall sales.</li>
        <li><a class="link-item" href="#Review_Analysis">Review Analysis</a>: Investigate customer reviews to gauge satisfaction levels, identify common issues, and enhance product quality and service.</li>
        <li><a class="link-item" href="#Order_Analysis">Order Analysis</a>: Dive into order trends, identify peak times, and analyze the volume and frequency of orders to improve inventory and marketing strategies.</li>
        <li><a class="link-item" href="#Products_Analysis">Products Analysis</a>: Explore product performance, identify top-selling and least-selling items, and assess the impact of product categories on sales.</li>
        <li><a class="link-item" href="#RFM_Analysis">RFM Analysis</a>: Segment customers based on Recency, Frequency, and Monetary value to tailor marketing efforts and increase customer retention.</li>
    </ul>

    Each analysis provides unique insights that can help optimize business strategies and drive better decision-making.
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    ### Unique Anonymization ✨

    This is real commercial data that has been anonymized. References to companies and partners in the review text have been creatively replaced with names from the Game of Thrones great houses.
    """)
    st.write("")
    st.markdown("""
    ### About Olist 🛍️

    Generously provided by Olist, this dataset offers a glimpse into the workings of Brazil's most extensive marketplace network. Olist connects small businesses from all over Brazil to various sales channels seamlessly, using a single contract. Merchants can sell their products through the Olist Store and ship them directly to customers using Olist's logistics partners.

    Learn more about Olist on our [website](https://www.olist.com).
    """)
    st.write("")
    st.markdown("""
    ### Customer Experience 👤

    After a customer purchases a product from the Olist Store, the seller is notified to fulfill the order. Once the product is delivered or the estimated delivery date has passed, the customer receives a satisfaction survey via email. They can rate their purchase experience and provide comments, enriching the dataset with valuable feedback.
    """)
    
    st.markdown("---")

    st.markdown("Explore the dashboard to uncover trends, analyze data, and make data-driven decisions with the Olist E-Commerce Data Analysis Dashboard!")

elif selected_option == "Dataset":
    st.title("Dataset 📂")
    st.markdown("#### This page is for viewing the dataset <br><br>", unsafe_allow_html=True)  
    try:
        view_all_df = pd.read_csv('data/all_data.csv')
        st.write("Dataset loaded successfully! ✨")
        st.write(view_all_df)
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        st.error("File is empty. Please check the file content.")
    except pd.errors.ParserError:
        st.error("File is corrupt or not a CSV. Please check the file format.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

elif selected_option == "Customer Analysis":
    st.title("Customer Analysis 👤")
    st.write("""Customer analysis based on city and state involves examining customer data
              to understand purchasing behavior, preferences, and trends within different geographical regions.
              This analysis can provide valuable insights for tailoring marketing strategies, optimizing inventory management, 
             and improving overall customer satisfaction<br><br>""", unsafe_allow_html=True)
    
    st.markdown("### 📍Top Customers by City")

    # Menghitung jumlah pelanggan unik per kota
    top_customer = all_df.groupby(by='customer_city')['customer_id'].nunique().sort_values(ascending=False)

    # Mengonversi ke DataFrame untuk kemudahan penggunaan dengan Plotly
    top_customer_df = top_customer.reset_index()
    top_customer_df.columns = ['customer_city', 'unique_customers']

    # Membuat bar chart untuk pelanggan teratas berdasarkan kota dengan Plotly Express
    fig = px.bar(top_customer_df.head(10), x='customer_city', y='unique_customers',
                labels={'customer_city': 'City', 'unique_customers': 'Number of Unique Customers'},
                color='unique_customers', color_continuous_scale=px.colors.sequential.Blues)

    # Menampilkan plot di Streamlit
    st.plotly_chart(fig)

    with st.expander("See explanation"):
        st.write(
            """
            The data represents the number of unique customers in various cities, sorted in descending order. Here’s a brief explanation of the top 10 cities based on unique customer counts:

            1. **Sao Paulo**: 15,540 unique customers. The largest city in the dataset with the highest number of customers.
            2. **Rio de Janeiro**: 6,882 unique customers. The second-largest city with a significant customer base.
            3. **Belo Horizonte**: 2,773 unique customers. A major city with a notable number of customers.
            4. **Brasilia**: 2,131 unique customers. The capital city with a strong customer presence.
            5. **Curitiba**: 1,521 unique customers. A large city with a substantial customer count.

            Cities further down in the top 10 would continue in decreasing order of unique customers. The data is sorted to highlight these top cities, showcasing where the largest customer bases are located.
            """
        )
    
    # Menghitung jumlah pelanggan unik per negara bagian
    customer_counts_by_state = all_df.groupby("customer_state").agg(
        {"customer_unique_id": "nunique"}
    ).reset_index().sort_values(by="customer_unique_id", ascending=False)

    st.markdown("### <br><br>📍Number of Unique Customers by State", unsafe_allow_html=True)

    # Membuat bar chart untuk distribusi pelanggan unik berdasarkan negara bagian dengan Plotly Graph Objects
    fig = go.Figure(data=[
        go.Bar(
            x=customer_counts_by_state['customer_state'],
            y=customer_counts_by_state['customer_unique_id'],
            marker=dict(
                color=customer_counts_by_state['customer_unique_id'],
                colorscale='Blues',  # Menggunakan palet warna 'Blues'
            )
        )
    ])

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Number of Unique Customers",
        xaxis_tickangle=-45  # Memutar label sumbu x agar tidak tumpang tindih
    )

    # Menampilkan plot di Streamlit
    st.plotly_chart(fig)
    with st.expander("See explanation"):
        st.write(
            """
            Here's a more detailed explanation of the data:

            - **São Paulo (SP)**: With 40,302 unique customers, São Paulo has the highest customer count, indicating it is a major market with significant customer activity.
            - **Rio de Janeiro (RJ)**: This state follows with 12,384 unique customers, showing it also has a substantial customer base, though less than São Paulo.
            - **Minas Gerais (MG)**: With 11,259 unique customers, Minas Gerais ranks third, reflecting a strong customer presence.

            The rest of the states have progressively fewer customers, with states like Acre (AC) having the smallest count of 77 unique customers. 

            **Observations:**
            - **Major Markets**: States like São Paulo, Rio de Janeiro, and Minas Gerais are key markets with the highest number of customers.
            - **Smaller Markets**: States such as Acre and Amapá have much smaller customer bases.

            This distribution can help businesses understand where their customer base is concentrated and potentially strategize targeted marketing or resource allocation based on regional customer density.
            """
        )

elif selected_option == "Geolocation Analysis":

    st.title("Geolocation Analysis 🗺️")
    st.write("This page shows the number of ZIP codes per city for the selected state. You can select a state from the dropdown menu to filter the data accordingly.")
    
    # Load data from CSV file
    geolocation_df = pd.read_csv('data/geolocation_dataset.csv')

    # Group by and count the size of each group
    grouped_df = geolocation_df.groupby(by=['geolocation_city', 'geolocation_state']).size().reset_index(name='count')

    # Select state to filter data
    state_options = grouped_df['geolocation_state'].unique()
    selected_state = st.selectbox("📍Select State", state_options)

    # Filter data based on the selected state
    filtered_df = grouped_df[grouped_df['geolocation_state'] == selected_state]

    # Create horizontal bar chart with Plotly Express
    fig = px.bar(
        filtered_df,
        y='geolocation_city',  # Y-axis: City
        x='count',  # X-axis: Count
        color='geolocation_state',  # Color by state
        orientation='h',  # Option for horizontal bar chart
        title=f'Number of ZIP Codes per City in {selected_state}',
        labels={'count': 'Number of ZIP Codes', 'geolocation_city': 'City'}
    )

    # Display plot in Streamlit
    st.plotly_chart(fig)

elif selected_option == "Payment Method Analysis":
    st.title("Payment Method Analysis 💸")
    st.write("""
    This page provides an analysis of the different payment methods used by customers. 
    We will look at the average payment value and the frequency of usage for each payment method. 
    Understanding these metrics can help us gain insights into customer preferences and behaviors.
    """)
    # Load the dataset
    order_payments_df = pd.read_csv('data/order_payments_dataset.csv')

    # DataFrame with average payment value
    avg_payment_value_by_type = order_payments_df.groupby("payment_type")["payment_value"].mean().reset_index()
    avg_payment_value_by_type.columns = ["Payment Type", "Average Payment Value"]

    # DataFrame with usage frequency
    payment_count_by_type = order_payments_df.groupby("payment_type")["order_id"].count().reset_index()
    payment_count_by_type.columns = ["Payment Type", "Transaction Count"]

    # Create a bar chart for average payment value
    fig_avg_payment = px.bar(
        avg_payment_value_by_type, 
        x="Payment Type", 
        y="Average Payment Value", 
        color="Payment Type", 
        title='💲Average Payment Value by Payment Type',
        labels={"Payment Type": "Payment Type", "Average Payment Value": "Average Value"}
    )

    # Create a bar chart for usage frequency
    fig_payment_count = px.bar(
        payment_count_by_type, 
        x="Payment Type", 
        y="Transaction Count", 
        color="Payment Type", 
        title='💲Usage Frequency by Payment Type',
        labels={"Payment Type": "Payment Type", "Transaction Count": "Transaction Count"}
    )

    # Display the charts in Streamlit
    st.plotly_chart(fig_avg_payment)
    st.plotly_chart(fig_payment_count)

    with st.expander("Analysis"):
        
        st.markdown("""
        **From the given data, we can draw several conclusions about the types of payments used and the average payment values:**

        1. **Average Payment Value**:
        - **`credit_card`** has the highest average payment value of **163.32**. This indicates that customers using credit cards tend to pay more per transaction compared to other payment methods.
        - **`boleto`** and **`debit_card`** have relatively close average payment values, at **145.03** and **142.57**, respectively. This shows that the average payment values for these two methods are almost the same.
        - **`voucher`** has the lowest average payment value at **65.70**, indicating that transactions using vouchers are typically smaller compared to other payment methods.
        - **`not_defined`** has an average payment value of **0.00**, which might indicate incomplete data or undefined transactions.

        2. **Usage Frequency**:
        - **`credit_card`** is the most frequently used payment method with **76,795** transactions. This shows that credit cards are the customers' preferred choice.
        - **`boleto`** is the second most popular payment method with **19,784** transactions. Although frequently used, its average payment value is lower compared to credit cards.
        - **`voucher`** and **`debit_card`** have much lower usage frequencies, with **5,775** and **1,529** transactions, respectively. This indicates that these two methods are not as popular as credit cards or boleto.
        - **`not_defined`** has a very low number of transactions (**3**), indicating that this data is almost negligible.
        """)

    st.markdown("#### <br>Question: What is the most frequently used payment method❓", unsafe_allow_html=True)
    with st.expander("Answer"):
        st.markdown("""
            - Credit card is the most frequently used payment method and also has the highest average payment value.
            - Boleto is a commonly used payment method but with a lower average payment value.
            - Voucher and debit card are less popular and have lower average payment values.
            - Data with not_defined may indicate issues or deficiencies in data collection.
        """)

elif selected_option == "Review Analysis":
   
    # Prepare data: calculate mean review scores for each product category
    data = (
        all_df.groupby("product_category_name_english")["review_score"]
        .mean()
        .reset_index()
    )
    data = data.sort_values(by="review_score", ascending=False)

    # Create a Plotly Express bar chart
    fig = px.bar(
        data,
        x="product_category_name_english",
        y="review_score",
        title="✏️ Distribution of Review Scores by Product Category",
        labels={"product_category_name_english": "Product Category", "review_score": "Review Score"},
        height=600
    )

    # Customize the chart
    fig.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Review Score",
        xaxis_tickangle=-90,  # Rotate x-axis labels for better readability
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        title_font_size=16
    )

    # Display the chart in Streamlit
    st.title("Distribution of Review Scores by Product Category 📝")
    st.write("""
    This bar chart shows the distribution of review scores across different product categories. 
    It helps in identifying which categories have higher average review scores.
    """)
    st.plotly_chart(fig)

    
    st.markdown("#### Question : Which products have good performance based on review ratings❓")


     # Calculate mean review scores for each product category and select the top 10
    mean_review_scores = all_df.groupby("product_category_name_english")["review_score"].mean().sort_values(ascending=False).nlargest(10)

    # Convert to DataFrame for plotting
    mean_review_scores_df = mean_review_scores.reset_index()
    fig = px.bar(
    mean_review_scores_df,
    y="product_category_name_english",  # Set y-axis for categories
    x="review_score",  # Set x-axis for average review scores
    orientation='h',  # Horizontal bars
    title="✏️ Top 10 Product Categories by Average Review Score",
    labels={"product_category_name_english": "Product Category", "review_score": "Average Review Score"},
    height=600
    )

    # Customize the chart
    fig.update_layout(
        xaxis_title="Average Review Score",
        yaxis_title="Product Category",
        yaxis_title_font_size=14,
        xaxis_title_font_size=14,
        title_font_size=16
    )

    st.plotly_chart(fig)

    with st.expander("Explanation"):
        data = {
        "Product Category": [
            "cds_dvds_musicals",
            "fashion_childrens_clothes",
            "books_general_interest",
            "costruction_tools_tools",
            "food_drink",
            "fashion_sport",
            "books_technical",
            "flowers",
            "books_imported",
            "luggage_accessories"
        ],
        "Average Review Score": [
            4.666667,
            4.500000,
            4.446768,
            4.425532,
            4.412955,
            4.411765,
            4.403636,
            4.392857,
            4.389831,
            4.333333
        ]
    }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Display the table in Streamlit
        st.dataframe(df, width=800)

        st.markdown("""
        **Product Categories with the Highest Review Scores:**

        - **cds_dvds_musicals** has the highest average review score of **4.67**. This indicates that customers are very satisfied with products in this category.
        - **fashion_childrens_clothes** also has a very high review score of **4.50**, indicating high customer satisfaction.

        **Popular Categories with High Review Scores:**

        - **books_general_interest**, **books_technical**, and **books_imported** have high review scores of **4.45**, **4.40**, and **4.39**, respectively. This shows that books in these categories generally receive very positive reviews.
        - **fashion_sport** with a score of **4.41** shows that sportswear products are also highly valued by customers.

        **Special Categories with High Review Scores:**

        - **costruction_tools_tools** with a score of **4.43** indicates that construction tools in this category perform well in the eyes of customers.
        - **food_drink** with a score of **4.41** shows that food and drinks in this category are highly valued.
        - **flowers** with a score of **4.39** indicates high customer satisfaction with flower products.
        - **luggage_accessories** with a score of **4.33** shows that luggage accessories have good performance in customer evaluations.

        **Customer Satisfaction:**

        Overall, the average review scores for these product categories are very high, indicating a good level of customer satisfaction. These categories might have good product quality, satisfactory customer service, or a combination of both.

        **Focus on High-Performing Products:**

        Increasing stock or focusing marketing efforts on high-review-score categories like **cds_dvds_musicals**, **fashion_childrens_clothes**, and **books_general_interest** could help further boost sales as they already have a solid customer base.
        """)

elif selected_option == "Order Analysis":

    st.title("Order Analysis 🛒")
    st.write("Order Analysis involves examining the data related to customer orders to identify trends, patterns, and insights that can help improve business performance.")
    st.write("")
    
    fig = px.histogram(
    all_df,
    x="order_status",
    color="order_status",  # Add color to differentiate categories
    title="",
    labels={"order_status": "Order Status"},
    color_discrete_sequence=px.colors.sequential.Viridis  # Optional: choose a color palette
    )

    # Update layout for better readability
    fig.update_layout(
        xaxis_title="Order Status",
        yaxis_title="Count",
        xaxis_tickangle=-45,  # Tilt x-axis labels for better readability
    )

    # Display the chart in Streamlit
    st.markdown("### 💡Distribution of Order Status")
    st.plotly_chart(fig)


    with st.expander("Analysis"):
        data = {
        "Order Status": ["delivered", "shipped", "canceled", "invoiced", "processing", "unavailable", "approved"],
        "Counts": [104335, 1204, 493, 357, 313, 7, 2]
        }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Display the table in Streamlit
        st.dataframe(df, width=800)

        # Provide the explanation
        st.markdown("""
        **Distribution of Order Status**

        1. **Delivered**: This status is the most common, with **100,777** orders marked as delivered. This indicates that the majority of orders have been successfully completed and delivered to customers.
        2. **Shipped**: There are **1,138** orders that have been shipped but not yet delivered. This status is the second most common and represents orders that are in transit.
        3. **Canceled**: **469** orders have been canceled. This might be due to various reasons such as customer requests, stock issues, or payment problems.
        4. **Invoiced**: There are **327** orders that have been invoiced, meaning the invoices have been generated, but the orders might still be in progress.
        5. **Processing**: **307** orders are still in the processing stage, indicating that they are being prepared for shipment or further actions.
        6. **Unavailable**: Only **7** orders are marked as unavailable, which might suggest that the products are out of stock or no longer available.
        7. **Approved**: **2** orders are in the approved status, which might indicate that they are approved for processing but have not yet moved to the next stage.

        This distribution provides insight into the current status of orders and can help in assessing the efficiency of the order fulfillment process.
        """)
    st.write("")
    # Load data
    order_items_df = pd.read_csv('data/order_items_dataset.csv')
    order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])

    # Extract year and month for grouping
    order_items_df['year'] = order_items_df['shipping_limit_date'].dt.strftime('%Y')
    order_items_df['month'] = order_items_df['shipping_limit_date'].dt.strftime('%m-%Y')
    sales = order_items_df.groupby(by=["month", "year"])["order_id"].nunique().reset_index()

    # Convert "month" to a datetime format
    sales["month"] = pd.to_datetime(sales["month"], format='%m-%Y')

    # Create Bullet Chart
    fig = go.Figure()

    # Add bullet trace
    fig.add_trace(go.Bar(
        x=sales["month"].dt.strftime('%b %Y'),
        y=sales["order_id"],
        name='Unique Orders',
        marker_color='royalblue'
    ))

    # Update layout
    fig.update_layout(
        title="",
        xaxis_title="Month",
        yaxis_title="Unique Orders",
        xaxis_tickformat="%b %Y",  # Format x-axis ticks as month and year
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        title_font_size=16,
        title_x=0.5,  # Center the title
        xaxis_tickangle=-45  # Tilt x-axis labels for better readability
    )

    # Display the chart in Streamlit
    st.markdown("### 💡Unique Orders per Month and Year")
    st.plotly_chart(fig)
    st.markdown("#### Question: When did the highest sales occur❓")
    with st.expander("Answer"):
        st.markdown("""
        1. **Highest Sales**:
        - The highest sales occurred in August 2018, with a total of `7823` orders. This indicates that this month had significantly higher sales activity compared to other months.

        2. **Seasonal Trends**:
        - In general, there is a seasonal pattern with higher sales in 2018 compared to other years, particularly in certain months such as March, May, and August. This suggests that 2018 was a very good year in terms of sales.

        3. **Yearly Comparison**:
        - The year 2018 consistently shows higher sales figures compared to other years, especially compared to 2017. This could indicate growth or an increase in sales in 2018.

        4. **Low Sales**:
        - Some months in 2020 show very low sales (e.g., February 2020 and April 2020). This may be related to external factors such as the impact of the COVID-19 pandemic or significant changes in business.

        5. **Inconsistent Data**:
        - There are data for non-consecutive years (e.g., 2016) showing very low sales, indicating that data from those years may not be as comprehensive as other years or may have recording issues.

        6. **Monthly Sales**:
        - Monthly sales show significant variation, with some months displaying large sales spikes. This indicates the possibility of seasonal fluctuations or special promotions affecting sales.

        Overall, the data shows that 2018 was a highly productive year in terms of sales, with August being the peak month. Meanwhile, there are other periods with low sales that may need further examination to understand the influencing factors.
        """)

elif selected_option == "Products Analysis":
    st.title("Product Sales Analysis 🛍️")
    st.write("")
    
    # Group by product_category_name_english and count product_id
    product_id_counts = all_df.groupby('product_category_name_english')['product_id'].count().reset_index()
    sorted_df = product_id_counts.sort_values(by='product_id', ascending=False)

    # Split data into top and bottom products
    top_products = sorted_df.head(5)
    bottom_products = sorted_df.tail(5).sort_values(by="product_id", ascending=False)

    # Create bar chart for top products using Plotly Express
    fig_top = px.bar(
        top_products,
        x="product_id",
        y="product_category_name_english",
        orientation='h',
        title="Products with the Highest Sales",
        labels={"product_id": "Number of Products Sold", "product_category_name_english": "Product Category"},
        color="product_id",
        color_continuous_scale=px.colors.sequential.Blues
    )

    # Update layout for better readability
    fig_top.update_layout(
        xaxis_title="Number of Products Sold",
        yaxis_title="Product Category",
        title_font_size=20,
        title_x=0.5,  # Center the title
        yaxis=dict(tickfont=dict(size=12))
    )

    # Create bar chart for bottom products using Plotly Express
    fig_bottom = px.bar(
        bottom_products,
        x="product_id",
        y="product_category_name_english",
        orientation='h',
        title="Products with the Lowest Sales",
        labels={"product_id": "Number of Products Sold", "product_category_name_english": "Product Category"},
        color="product_id",
        color_continuous_scale=px.colors.sequential.Reds
    )

    # Update layout for better readability
    fig_bottom.update_layout(
        xaxis_title="Number of Products Sold",
        yaxis_title="Product Category",
        title_font_size=20,
        title_x=0.5,  # Center the title
        yaxis=dict(tickfont=dict(size=12))
    )

    tab1, tab2 = st.tabs(["The Most Sold Products 🔎", "The Least Sold Products 🔎"])

    with tab1:
        st.plotly_chart(fig_top)

    with tab2:
        st.plotly_chart(fig_bottom)
    
    with st.expander("Analysis"):
        st.write("""
        1. **Categories with the Most Products**:
        - **Bed_Bath_Table**: This category has the highest number of products with a `product_id` count of 11,105.
        - **Health_Beauty**: This category is also very popular with a `product_id` count of 9,426.
        - **Sports_Leisure**: This category has a significant number of products with a `product_id` count of 8,286.
        - **Computers_Accessories**: This category has a high number of products with a `product_id` count of 7,286.
        - **Furniture_Decor**: This category has a large number of products with a `product_id` count of 7,222.
        
        2. **Categories with the Fewest Products**:
        - **Security and Services**: This category has the fewest number of products with a `product_id` count of 2.
        - **PC Gaming** and **Fashion Children's Clothes**: Both of these categories have very few products with a `product_id` count of 8.
        - **CDs, DVDs, Musicals**: This category has a very low number of products with a `product_id` count of 12.
        - **La Cuisine**: This category also has very few products with a `product_id` count of 13.
        
        3. **Product Distribution**:
        - Categories related to home and health (such as `bed_bath_table` and `health_beauty`) tend to have more products.
        - More specific or niche categories (such as `security_and_services` and `PC Gaming`) have fewer products.
        
        4. **Product Category Analysis**:
        - Categories with a large number of products likely reflect high popularity or demand in those categories.
        - Categories with a few products may reflect niche markets or very specific product categories with limited demand.
        """)

elif selected_option == "RFM Analysis":
    st.title("RFM Analysis 📈")
    st.write("""
    **RFM (Recency, Frequency, Monetary) Analysis** is a method used to segment customers based on how frequently and how much they spend. Here's what each component means:

    1. **Recency**: How recent was the customer's last purchase. Customers who have bought recently have a higher recency value.

    2. **Frequency**: How often the customer makes a purchase. Customers who buy frequently have a higher frequency value.

    3. **Monetary**: How much money the customer spends. Customers who spend more have a higher monetary value.

    By using RFM analysis, businesses can score each customer based on these three factors. This helps businesses to segment customers into categories such as loyal customers, those who need attention, or those who are almost inactive, allowing targeted marketing efforts and appropriate offers.
    """)

    orders_df = pd.read_csv('data\orders_dataset.csv')
    orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])

    # Calculate total price for each order
    all_df["total_price"] = all_df["price"] * all_df["quantity"]

    # Create RFM DataFrame
    rfm_df = all_df.groupby("customer_unique_id", as_index=False).agg(
        {"order_purchase_timestamp": "max",  # Last order date
        "order_id": "nunique",              # Frequency of unique orders
        "total_price": "sum"}               # Monetary value
    )

    # Rename columns for clarity
    rfm_df.columns = ["customer_unique_id", "last_order_date", "frequency", "monetary"]

    # Convert 'last_order_date' to datetime
    rfm_df["last_order_date"] = pd.to_datetime(rfm_df["last_order_date"])

    # Get the most recent order date
    recent_date = pd.to_datetime(orders_df["order_purchase_timestamp"].dt.date.max())

    # Calculate recency
    rfm_df["recency"] = (recent_date - rfm_df["last_order_date"]).dt.days

    # Drop 'last_order_date' column
    rfm_df.drop("last_order_date", axis=1, inplace=True)

    # Calculate RFM scores
    rfm_df["r_rank"] = rfm_df["recency"].rank(ascending=False)
    rfm_df["f_rank"] = rfm_df["frequency"].rank(ascending=True)
    rfm_df["m_rank"] = rfm_df["monetary"].rank(ascending=True)

    # Normalize RFM ranks
    for col in ["r_rank", "f_rank", "m_rank"]:
        rfm_df[f"{col}_norm"] = (rfm_df[col] / rfm_df[col].max()) * 100

    # Calculate final RFM score
    rfm_df["RFM_score"] = (
        0.15 * rfm_df["r_rank_norm"]
        + 0.28 * rfm_df["f_rank_norm"]
        + 0.57 * rfm_df["m_rank_norm"]
    ) * 0.05

    # Round RFM score
    rfm_df["RFM_score"] = rfm_df["RFM_score"].round(2)

    # Define customer segments
    def map_customer_segment(score):
        if score > 3:
            return "Top Customers"
        elif score > 2.5:
            return "High Value Customers"
        elif score > 2:
            return "Mid Value Customers"
        elif score > 1:
            return "Low Value Customers"
        else:
            return "Lost Customers"

    rfm_df["customer_segment"] = rfm_df["RFM_score"].apply(map_customer_segment)

    # Count unique customers per segment
    customer_segment_df = rfm_df.groupby("customer_segment")["customer_unique_id"].nunique().reset_index()

    # Define the order for the customer segments
    customer_segment_df["customer_segment"] = pd.Categorical(
        customer_segment_df["customer_segment"],
        categories=[
            "Top Customers",
            "High Value Customers",
            "Mid Value Customers",
            "Low Value Customers",
            "Lost Customers"
        ],
        ordered=True
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📌Recency", "📌Frequency", "📌Monetary", "📌RFM Scores", "📌Customer Segments"])

    # Recency
    with tab1:
        st.header("Top 5 Customers by Recency")
        top_customers = rfm_df.sort_values(by="recency", ascending=True).head(5)
        fig_recency = px.bar(
            top_customers,
            x="recency",
            y="customer_unique_id",
            orientation='h',
            title="Top 5 Customers by Recency",
            labels={"recency": "Recency (Days Since Last Purchase)", "customer_unique_id": "Customer ID"},
            color="recency",
            color_continuous_scale=px.colors.sequential.Blues
        )
        st.plotly_chart(fig_recency)

    # Frequency
    with tab2:
        st.header("Top 5 Customers by Frequency")
        top_customers_freq = rfm_df.sort_values(by="frequency", ascending=False).head(5)
        fig_frequency = px.bar(
            top_customers_freq,
            x="frequency",
            y="customer_unique_id",
            orientation='h',
            title="Top 5 Customers by Frequency",
            labels={"frequency": "Frequency (Number of Orders)", "customer_unique_id": "Customer ID"},
            color="frequency",
            color_continuous_scale=px.colors.sequential.Greens
        )
        st.plotly_chart(fig_frequency)

    # Monetary
    with tab3:
        st.header("Top 5 Customers by Monetary")
        top_customers_monetary = rfm_df.sort_values(by="monetary", ascending=False).head(5)
        fig_monetary = px.bar(
            top_customers_monetary,
            x="monetary",
            y="customer_unique_id",
            orientation='h',
            title="Top 5 Customers by Monetary",
            labels={"monetary": "Monetary Value (Total Spend)", "customer_unique_id": "Customer ID"},
            color="monetary",
            color_continuous_scale=px.colors.sequential.Reds
        )
        st.plotly_chart(fig_monetary)

    # RFM Scores
    with tab4:
        st.header("Top 5 Customers by RFM Score")
        top_customers_rfm = rfm_df.sort_values(by="RFM_score", ascending=False).head(5)
        fig_rfm_score = px.bar(
            top_customers_rfm,
            x="RFM_score",
            y="customer_unique_id",
            orientation='h',
            title="Top 5 Customers by RFM Score",
            labels={"RFM_score": "RFM Score", "customer_unique_id": "Customer ID"},
            color="RFM_score",
            color_continuous_scale=px.colors.sequential.Plasma
        )
        st.plotly_chart(fig_rfm_score)

    # Customer Segments
    with tab5:
        st.header("Customer Segments Distribution")
        fig_customer_segments = px.bar(
            customer_segment_df,
            x="customer_segment",
            y="customer_unique_id",
            title="Number of Customers per Segment",
            labels={"customer_segment": "Customer Segment", "customer_unique_id": "Number of Customers"},
            color="customer_segment",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_customer_segments)

    with st.expander("RFM Analysis Explanation"):
        st.write("""
        
            ***RFM Analysis provides a numerical ranking for customers in five categories, where higher numbers indicate better results:***

        1. **Top Customers**: Customers who have bought most recently, most frequently, and spent the most.
        2. **High Value Customers**: Customers who buy most frequently and spend the most.
        3. **Middle Value Customers**: Customers who have bought most recently and spent the most.
        4. **Low Value Customers**: Customers who have bought most recently, most frequently, but spent the least.
        5. **Lost Customers**: Customers who haven't made a purchase for the longest time
        """)

    with st.expander("Conclusion"):
        st.write("""
        
            1. **Top Customers:**
            - There are 31,050 customers in this segment, the highest among all segments. This indicates that many customers are highly active, having bought recently, frequently, and spent a significant amount of money.

            2. **Low Value Customers:**
            - This segment includes 29,620 customers, also a significant number. Customers in this category have bought recently and frequently but spend less compared to Top Customers.

            3. **Mid Value Customers:**
            - There are 16,262 customers in this segment. They have bought recently and spent a lot, but they are not as active as Top or Low Value Customers in terms of purchase frequency.

            4. **High Value Customers:**
            - This segment contains 16,014 customers. They buy most frequently and spend a lot, but they do not purchase as often or recently as Top or Low Value Customers.

            5. **Lost Customers:**
            - With only 2,474 customers, this segment has the smallest number. This indicates that relatively few customers have not made a purchase for a long time.

            **Analysis:**

            - **Top Customers** and **Low Value Customers** have significant numbers, suggesting there are many active and frequent buyers with varying spending levels.
        
            - **Mid Value Customers** and **High Value Customers** are fewer compared to the other two active segments but show high spending value.
        
            - **Lost Customers** are the smallest group, indicating that only a small proportion of customers have not purchased for a long period.
        """)

# -------------------------------------------COPYRIGHT---------------------------------------------------------------
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        &copy; 2024 Olist E-Commerce Data Analysis Dashboard by Fulgencia Shaynalie Rue. All rights reserved.
    </div>
    """, unsafe_allow_html=True)