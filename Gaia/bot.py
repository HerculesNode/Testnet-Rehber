import requests
import random
import time
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Configuration
BASE_URL = "https://qavurdagli.gaia.domains"
MODEL = "qwen2-0.5b-instruct"
MAX_RETRIES = 100  # Essentially infinite retries
RETRY_DELAY = 5  # Seconds between retries
QUESTION_DELAY = 1  # Seconds between successful questions

QUESTIONS = [
"How to design and build websites using no-code." ,
"What are the benefits of using no-code platforms for website building?" ,
"What are the most popular no-code website builders currently available?" ,
"How do I choose the right no-code website builder for my project?" ,
"How do I get started with designing my website on a no-code platform?" ,
"How do I add pages, navigation, and other elements to my website using a no-code platform?" ,
"How do I customize the look and feel of my website using a no-code platform?" ,
"What options do I have for integrating third-party tools and services into my website using no-code?" ,
"How do I make sure my website is mobile-friendly using a no-code platform?" ,
"What steps do I need to take to launch my website using a no-code platform?" ,
"Can I use a no-code platform to build an e-commerce website?" ,
"What are the limitations of using a no-code platform to build a website?" ,
"How do I handle SEO for my website when using a no-code platform?" ,
"What resources are available to help me learn more about using no-code for website building?" ,
"Can I hire a professional to help me build my website using a no-code platform?" ,
"How much does it cost to build a website using a no-code platform?" ,
"Can I create a custom domain for my website using a no-code platform?" ,
"How can I get support if I run into issues while building my website using a no-code platform?" ,
"How do I maintain and update my website after it has been built using a no-code platform?" ,
"What are some examples of websites built using no-code platforms?" ,
"What kind of websites can be built using a no-code platform?" ,
"How do I add custom code to my website if needed when using a no-code platform?" ,
"How can I add forms and other interactive elements to my website using a no-code platform?" ,
"What options do I have for hosting my website when using a no-code platform?" ,
"How can I use no-code to create a landing page for my website?" ,
"How do I make sure my website is accessible and inclusive using a no-code platform?" ,
"How do I add and manage images and other media on my website using a no-code platform?" ,
"How can I add blog functionality to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a business or organization?" ,
"How do I add e-mail sign-up forms and newsletters to my website using a no-code platform?" ,
"How can I track website analytics using a no-code platform?" ,
"Can I use a no-code platform to build a portfolio website for my creative work?" ,
"How can I add social media integration to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a non-profit organization?" ,
"How can I add a search function to my website using a no-code platform?" ,
"How do I ensure the security of my website when using a no-code platform?" ,
"What is the process for publishing and launching a website using a no-code platform?" ,
"How can I integrate payment systems into my e-commerce website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a local business or small enterprise?" ,
"How do I ensure that my website loads quickly and efficiently when using a no-code platform?" ,
"How do I add a custom favicon to my website using a no-code platform?" ,
"How can I add Google Maps integration to my website using a no-code platform?" ,
"What options do I have for integrating email marketing into my website using a no-code platform?" ,
"How do I add customer reviews and testimonials to my website using a no-code platform?" ,
"How can I add a contact form to my website using a no-code platform?" ,
"What resources are available to help me troubleshoot issues while building my website using a no-code platform?" ,
"How can I use a no-code platform to create a website for a community or social network?" ,
"How can I add a photo gallery to my website using a no-code platform?" ,
"What options do I have for adding custom fonts and typography to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a personal blog or diary?" ,
"How can I optimize my website for search engines using a no-code platform?" ,
"How to use no-code for building applications." ,
"What are the benefits of using no-code for building applications?" ,
"What kind of applications can be built using no-code platforms?" ,
"What are the most popular no-code platforms for building applications?" ,
"How do I choose the right no-code platform for building my application?" ,
"How do I get started with designing my application using a no-code platform?" ,
"How do I add and manage data in my application using a no-code platform?" ,
"What options do I have for integrating third-party services into my application using no-code?" ,
"How do I customize the user interface of my application using a no-code platform?" ,
"How do I add and manage users in my application using a no-code platform?" ,
"How do I handle security and privacy when building an application using a no-code platform?" ,
"How do I handle user authentication and authorization in my application using a no-code platform?" ,
"How do I test and debug my application when using a no-code platform?" ,
"How do I handle deployment and hosting of my application when using a no-code platform?" ,
"How do I handle data migration when building an application using a no-code platform?" ,
"Can I add custom code to my application when using a no-code platform?" ,
"How do I add user-generated content to my application using a no-code platform?" ,
"How do I handle scalability and performance when building an application using a no-code platform?" ,
"Can I use a no-code platform to build a mobile application?" ,
"How do I handle payments and billing when building an application using a no-code platform?" ,
"How do I handle email and SMS notifications in my application using a no-code platform?" ,
"How do I handle push notifications in my application using a no-code platform?" ,
"How do I handle user analytics and tracking in my application using a no-code platform?" ,
"How do I handle error handling and exception handling in my application using a no-code platform?" ,
"How do I handle user feedback and bug reporting in my application using a no-code platform?" ,
"How do I handle integration with external APIs in my application using a no-code platform?" ,
"What resources are available to help me learn more about using no-code for application building?" ,
"How do I handle database management in my application when using a no-code platform?" ,
"Can I use a no-code platform to build a real-time application?" ,
"How do I handle user roles and permissions in my application using a no-code platform?" ,
"How do I handle user privacy and data protection in my application using a no-code platform?" ,
"How do I handle version control and collaboration when building an application using a no-code platform?" ,
"How do I handle backups and disaster recovery in my application using a no-code platform?" ,
"How do I handle updates and maintenance for my application using a no-code platform?" ,
"Can I use a no-code platform to build an enterprise-level application?" ,
"How do I handle integration with other applications and systems in my application using a no-code platform?" ,
"How do I handle integration with social media platforms in my application using a no-code platform?" ,
"How do I handle performance optimization in my application using a no-code platform?" ,
"How do I handle user engagement" ,
"How do I handle user segmentation and targeting in my application using a no-code platform?" ,
"How do I handle user personalization in my application using a no-code platform?" ,
"How do I handle user onboarding in my application using a no-code platform?" ,
"How do I handle user retention in my application using a no-code platform?" ,
"How do I handle user feedback and support in my application using a no-code platform?" ,
"How do I handle integration with customer relationship management (CRM) systems in my application using a no-code platform?" ,
"How do I handle integration with marketing automation systems in my application using a no-code platform?" ,
"How do I handle internationalization and localization in my application using a no-code platform?" ,
"How do I handle data privacy and compliance when building an application using a no-code platform?" ,
"How do I handle data visualization and reporting in my application using a no-code platform?" ,
"How do I handle integration with cloud storage and file sharing systems in my application using a no-code platform?" ,
"How do I handle integration with project management and task management systems in my application using a no-code platform?" ,
"How to scale your no-code business." ,
"What are the key factors to consider when scaling a no-code business?" ,
"What are the most common challenges faced when scaling a no-code business?" ,
"What are the best practices for scaling a no-code business?" ,
"How do I measure the success of my no-code business?" ,
"How do I determine when it is the right time to scale my no-code business?" ,
"What are the key metrics to track when scaling a no-code business?" ,
"How do I attract and retain customers when scaling my no-code business?" ,
"How do I build a strong brand for my no-code business?" ,
"How do I build a strong team for my no-code business?" ,
"What are the most effective marketing strategies for scaling a no-code business?" ,
"How do I build a sustainable revenue model for my no-code business?" ,
"How do I scale my customer support operations when scaling my no-code business?" ,
"How do I build a culture of innovation and creativity in my no-code business?" ,
"How do I handle growth and expansion in my no-code business?" ,
"How do I handle competition in my no-code business?" ,
"What are the best tools and resources for scaling a no-code business?" ,
"How do I handle financial management and budgeting when scaling my no-code business?" ,
"How do I handle legal and regulatory issues when scaling my no-code business?" ,
"How do I handle data management and data privacy when scaling my no-code business?" ,
"How do I handle security and privacy when scaling my no-code business?" ,
"How do I handle infrastructure and technology management when scaling my no-code business?" ,
"How do I handle product development and innovation when scaling my no-code business?" ,
"How do I handle user engagement and retention when scaling my no-code business?" ,
"How do I handle user feedback and support when scaling my no-code business?" ,
"How do I handle user acquisition and marketing when scaling my no-code business?" ,
"How do I handle user onboarding and training when scaling my no-code business?" ,
"How do I handle user growth and scaling when scaling my no-code business?" ,
"How do I handle partnerships and collaborations when scaling my no-code business?" ,
"How do I handle fundraising and investment when scaling my no-code business?" ,
"How do I handle international expansion when scaling my no-code business?" ,
"How do I handle business operations and management when scaling my no-code business?" ,
"How do I handle product management when scaling my no-code business?" ,
"How do I handle marketing and sales when scaling my no-code business?" ,
"How do I handle customer support and service when scaling my no-code business?" ,
"How do I handle organizational growth and development when scaling my no-code business?" ,
"How do I handle team building and management when scaling my no-code business?" ,
"How do I handle business process automation when scaling my no-code business?" ,
"How do I handle remote work and virtual teams when scaling my no-code business?" ,
"How do I handle hiring and talent management when scaling my no-code business?" ,
"How do I handle project management and task management when scaling my no-code business?" ,
"How do I handle risk management and crisis management when scaling my no" ,
"How can I optimize my no-code business's revenue model to increase growth?" ,
"How do I ensure that my customer support operations are able to handle increased demand?" ,
"How do I create and implement an effective marketing strategy to attract new customers?" ,
"What are the best ways to scale and manage my team as my no-code business grows?" ,
"How can I establish a strong brand identity to differentiate my no-code business from the competition?" ,
"How do I plan and manage financial resources as my no-code business grows?" ,
"What are the key considerations for expanding internationally, and how do I plan for it?" ,
"How do I keep up with the latest technology trends and innovations to maintain a competitive edge?" ,
"What steps can I take to streamline business operations and improve efficiency as my no-code business grows?" ,
"How to do SEO using no-code." ,
"What is the significance of SEO in no-code?" ,
"What are the most important factors for SEO in no-code?" ,
"How do I optimize my no-code website for search engines?" ,
"What are the best tools and resources for SEO in no-code?" ,
"How do I conduct keyword research for my no-code website?" ,
"What are the best practices for on-page optimization in no-code?" ,
"How do I optimize my website's meta tags for SEO in no-code?" ,
"How do I optimize my website's content for SEO in no-code?" ,
"How do I optimize my website's images for SEO in no-code?" ,
"How do I optimize my website's internal linking for SEO in no-code?" ,
"What are the best strategies for building high-quality backlinks for SEO in no-code?" ,
"How do I track and measure my SEO results in no-code?" ,
"How do I handle technical SEO in no-code?" ,
"How do I handle mobile optimization for SEO in no-code?" ,
"How do I handle local SEO in no-code?" ,
"How do I handle voice search optimization in no-code?" ,
"How do I handle schema markup for SEO in no-code?" ,
"How do I handle website speed and performance optimization for SEO in no-code?" ,
"How do I handle content marketing for SEO in no-code?" ,
"How do I handle link building for SEO in no-code?" ,
"How do I handle social media optimization for SEO in no-code?" ,
"How do I handle video optimization for SEO in no-code?" ,
"How do I handle site structure optimization for SEO in no-code?" ,
"How do I handle website design for SEO in no-code?" ,
"How do I handle website security for SEO in no-code?" ,
"How do I handle website accessibility for SEO in no-code?" ,
"How do I handle website migration for SEO in no-code?" ,
"How do I handle website redirects for SEO in no-code?" ,
"How do I handle website copywriting for SEO in no-code?" ,
"How do I handle website analytics for SEO in no-code?" ,
"How do I handle website testing and experimentation for SEO in no-code?" ,
"How do I handle website user experience for SEO in no-code?" ,
"How do I handle website content strategy for SEO in no-code?" ,
"How do I handle website audience targeting for SEO in no-code?" ,
"How do I handle website language optimization for SEO in no-code?" ,
"How do I handle website conversion rate optimization for SEO in no-code?" ,
"How do I handle website marketing automation for SEO in no-code?" ,
"How do I handle website personalization for SEO in no-code?" ,
"How do I handle website social proof for SEO in no-code?" ,
"How do I handle website lead generation for SEO in no-code?" ,
"How do I handle website branding for SEO in no-code?" ,
"How do I handle website reputation management for SEO in no-code?" ,
"How do I handle website ad targeting for SEO in no-code?" ,
"How do I handle website customer feedback for SEO in no-code?" ,
"How do I handle website accessibility and crawlability for SEO in no-code?" ,
"How do I optimize my website's URLs for SEO in no-code?" ,
"How do I implement structured data and schema markup for SEO in no-code?" ,
"How do I create and optimize content for featured snippets for SEO in no-code?" ,
"How do I use header tags (H1, H2, H3, etc.) to improve my website's SEO in no-code?" ,
"How do I perform competitive analysis to improve my website's SEO in no-code?" ,
"How to optimize workflow automation." ,
"What is the significance of workflow automation in no-code?" ,
"What are the most important benefits of workflow automation in no-code?" ,
"How do I automate repetitive tasks using no-code?" ,
"What are the best tools and resources for workflow automation in no-code?" ,
"How do I identify opportunities for workflow automation in no-code?" ,
"How do I create and manage workflows in no-code?" ,
"How do I optimize workflows for efficiency and productivity in no-code?" ,
"How do I automate data entry and data management in no-code?" ,
"How do I automate email communication in no-code?" ,
"How do I automate document management in no-code?" ,
"How do I automate project management in no-code?" ,
"How do I automate customer relationship management in no-code?" ,
"How do I automate sales processes in no-code?" ,
"How do I automate marketing processes in no-code?" ,
"How do I automate human resource processes in no-code?" ,
"How do I automate finance and accounting processes in no-code?" ,
"How do I integrate workflow automation with other tools and systems in no-code?" ,
"How do I monitor and analyze workflow automation results in no-code?" ,
"How do I troubleshoot and fix errors in workflow automation in no-code?" ,
"How do I optimize workflows for scalability in no-code?" ,
"How do I optimize workflows for collaboration and teamwork in no-code?" ,
"How do I optimize workflows for security and privacy in no-code?" ,
"How do I optimize workflows for user experience in no-code?" ,
"How do I optimize workflows for accessibility in no-code?" ,
"How do I optimize workflows for user adoption in no-code?" ,
"How do I optimize workflows for data accuracy and consistency in no-code?" ,
"How do I optimize workflows for data processing speed in no-code?" ,
"How do I optimize workflows for data privacy and security in no-code?" ,
"How do I optimize workflows for data storage and retrieval in no-code?" ,
"How do I optimize workflows for data management and organization in no-code?" ,
"How do I optimize workflows for data analysis and reporting in no-code?" ,
"How do I optimize workflows for data backup and recovery in no-code?" ,
"How do I optimize workflows for data sharing and collaboration in no-code?" ,
"How do I optimize workflows for data integration and migration in no-code?" ,
"How do I optimize workflows for data quality control in no-code?" ,
"How do I optimize workflows for data validation and error checking in no-code?" ,
"How do I optimize workflows for data security and compliance in no-code?" ,
"How do I optimize workflows for data visualization and representation in no-code?" ,
"How do I optimize workflows for data tracking and monitoring in no-code?" ,
"How do I optimize workflows for data analysis and optimization in no-code?" ,
"How do I optimize workflows for data management and administration in no-code?" ,
"How do I optimize workflows for data governance and management in no-code?" ,
"How do I optimize workflows for data discovery and exploration in no-code?" ,
"How do I implement conditional logic in workflow automation in no-code?" ,
"How do I automate tasks based on triggers and events in no-code?" ,
"How do I automate tasks based on data inputs and outputs in no-code?" ,
"How do I implement error handling and recovery in workflow automation in no-code?" ,
"How do I optimize workflows for automation performance and speed in no-code?" ,
"How do I optimize workflows for integration with other software and systems in no-code?" ,
"How do I measure and improve the success rate of workflow automation in no-code?" ,
"How to do database creation." ,
"How do I create a database in no-code?" ,
"How do I design the schema of a database in no-code?" ,
"How do I add, edit, and delete records in a database in no-code?" ,
"How do I implement relationships between tables in a database in no-code?" ,
"How do I perform basic database operations, such as CRUD, in no-code?" ,
"How do I query and filter data in a database in no-code?" ,
"How do I perform database aggregations, such as summing and averaging, in no-code?" ,
"How do I import and export data from a database in no-code?" ,
"How do I perform database backups and restores in no-code?" ,
"How do I manage database users and permissions in no-code?" ,
"How do I implement database security in no-code?" ,
"How do I optimize database performance in no-code?" ,
"How do I integrate a database with other applications and services in no-code?" ,
"How do I visualize and present data from a database in no-code?" ,
"How do I use databases with form submissions and user inputs in no-code?" ,
"How do I create reports and dashboards based on data in a database in no-code?" ,
"How do I implement database triggers and events in no-code?" ,
"How do I integrate databases with third-party APIs in no-code?" ,
"How do I store and manage large amounts of data in a database in no-code?" ,
"How do I implement full-text search in a database in no-code?" ,
"How do I implement database indexing and caching for performance in no-code?" ,
"How do I implement database transactions and rollbacks in no-code?" ,
"How do I implement database versioning and migration in no-code?" ,
"How do I manage database dependencies and configurations in no-code?" ,
"How do I perform database testing and debugging in no-code?" ,
"How do I implement database-driven user authentication and authorization in no-code?" ,
"How do I store and manage metadata in a database in no-code?" ,
"How do I store and manage media and files in a database in no-code?" ,
"How do I implement database-driven e-commerce functionality in no-code?" ,
"How do I implement database-driven multi-language support in no-code?" ,
"How do I integrate databases with mobile applications in no-code?" ,
"How do I implement database-driven real-time functionality in no-code?" ,
"How do I implement database-driven machine learning models in no-code?" ,
"How do I store and manage geolocation data in a database in no-code?" ,
"How do I store and manage time-series data in a database in no-code?" ,
"How do I store and manage unstructured data in a database in no-code?" ,
"How do I store and manage complex data structures, such as graphs and trees, in a database in no-code?" ,
"How do I store and manage hierarchical data in a database in no-code?" ,
"How do I implement database-driven content management in no-code?" ,
"How do I store and manage user-generated content in a database in no-code?" ,
"How do I implement database-driven data validation in no-code?" ,
"How do I store and manage user preferences and settings in a database in no-code?" ,
"How do I implement database-driven recommendations and personalized content in no-code?" ,
"How do I implement database-driven data analysis and data warehousing in no-code?" ,
"How do I implement database-driven data integration and data warehousing in no-code?" ,
"How do I implement database-driven data governance and data management in no-code?" ,
"How do I implement database-driven data privacy and security in no-code?" ,
"How do I implement database-driven data archiving and data retention in no-code?" ,
"How do I implement database-driven data migration and data transfer in no-code?" ,
"How do I implement database-driven data reporting and data visualization in no-code?"
]

def chat_with_ai(api_key: str, question: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {"role": "user", "content": question}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt+1} for question: {question[:50]}...")
            response = requests.post(
                f"{BASE_URL}/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            logging.warning(f"API Error ({response.status_code}): {response.text}")
            time.sleep(RETRY_DELAY)

        except Exception as e:
            logging.error(f"Request failed: {str(e)}")
            time.sleep(RETRY_DELAY)

    raise Exception("Max retries exceeded")

def run_bot(api_key: str):
    while True:  # Outer loop to repeat the questions indefinitely
        random.shuffle(QUESTIONS)
        logging.info(f"Starting chatbot with {len(QUESTIONS)} questions in random order")

        for i, question in enumerate(QUESTIONS, 1):
            logging.info(f"\nProcessing question {i}/{len(QUESTIONS)}")
            logging.info(f"Question: {question}")

            start_time = time.time()
            try:
                response = chat_with_ai(api_key, question)
                elapsed = time.time() - start_time

                # Print the entire response
                print(f"Answer to '{question[:50]}...':\n{response}")

                logging.info(f"Received full response in {elapsed:.2f}s")
                logging.info(f"Response length: {len(response)} characters")

                # Ensure the script waits for the full response before proceeding
                time.sleep(QUESTION_DELAY)  # Wait before asking next question

            except Exception as e:
                logging.error(f"Failed to process question: {str(e)}")
                continue

def main():
    print("Title: GaiaAI Chatbot")
    print("Created by: HerculesNode")
    print("Twitter: https://x.com/herculesnode")
    api_key = input("Enter your API key: Gaia ile baslayacak ")
    run_bot(api_key)

if __name__ == "__main__":
    main()
