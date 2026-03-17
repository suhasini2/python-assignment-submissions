1. Explain why databases are important in real-world AI systems. Mention examples of the types of data typically stored in databases and why structured storage is necessary.

Ans:- 
Why databases are important in real-world AI systems
Most AI systems  (like LLM) don't know everything, Database allow them to pull in specific, real-time facts/ results. Databases allow systems to query this information in milliseconds rather than searching through flat files.

Types of Data Stored
Vector Embeddings: Mathematical representations of text or images that allow AI to find "similar" concepts.
User Profiles: Preferences, past interactions, and metadata that help personalize AI responses.
Training Datasets: Massive collections of cleaned text, sensor logs, or labeled images used for fine-tuning.
Feedback Loops: Data on whether an AI's output was helpful, used to improve future performance. 

The Necessity of Structured Storage 
Structured storage (like SQL or specialized Vector Databases) is essential because AI requires consistency and speed. Without a structure: 
Search becomes impossible: You can't perform complex filtering (e.g., "find all customer complaints from June involving product X") efficiently.
Data Integrity fails: Structured schemas ensure that the AI isn't consuming "garbage" data (missing fields, wrong formats) that could cause the model to hallucinate or crash.
Concurrency: Databases allow thousands of users to interact with the AI simultaneously without the data becoming corrupted or locked.

2. Describe the relational database mental model. Explain what tables, rows, and columns represent, and why each table should represent a single entity.

Ans:-
The relational database mental model is best pictured as a collection of interconnected spreadsheets. It’s built on the idea that data should be organized logically to avoid repetition and ensure accuracy. 
The Breakdown
Tables (Entities): Think of a table as a specific category or "bucket" of things, like Customers, Orders, or Products.
Rows (Records): A row represents a single, unique instance of that entity. If the table is Customers, one row is exactly one human being.
Columns (Attributes): Columns define the specific traits or pieces of data that every record in that table must have, such as a Phone Number, Email, or Birthdate. 
Why One Table = One Entity?
In a well-designed database, each table follows the "Single Responsibility Principle." Here is why that matters: 
Redundancy (The "Update" Problem): If you store a customer’s address in every single Order row, and that customer moves, you have to update 50 rows. If the address is in its own Customer table, you update it once.
Accuracy (Data Integrity): It prevents "partial" data. You shouldn’t have to create a fake "Order" just to add a new "Customer" to your system.
Relationships: By keeping entities separate, you can link them using Keys. A Customer ID in the Orders table acts as a pointer, letting the database instantly connect a purchase to a person without duplicating their profile info

3. Explain the concept of a primary key. Describe why primary keys must be unique and non-null, and how they help identify records in a table.

Ans:-
The relational database mental model is best pictured as a collection of interconnected spreadsheets. It’s built on the idea that data should be organized logically to avoid repetition and ensure accuracy. 
The Breakdown
Tables (Entities): Think of a table as a specific category or "bucket" of things, like Customers, Orders, or Products.
Rows (Records): A row represents a single, unique instance of that entity. If the table is Customers, one row is exactly one human being.
Columns (Attributes): Columns define the specific traits or pieces of data that every record in that table must have, such as a Phone Number, Email, or Birthdate. 
Why One Table = One Entity?
In a well-designed database, each table follows the "Single Responsibility Principle." Here is why that matters: 
Redundancy (The "Update" Problem): If you store a customer’s address in every single Order row, and that customer moves, you have to update 50 rows. If the address is in its own Customer table, you update it once.
Accuracy (Data Integrity): It prevents "partial" data. You shouldn’t have to create a fake "Order" just to add a new "Customer" to your system.
Relationships: By keeping entities separate, you can link them using Keys. A Customer ID in the Orders table acts as a pointer, letting the database instantly connect a purchase to a person without duplicating their profile info. 
Example for Primary key
Imagine a Students table at a university. Even if two students are both named "Alice Smith" and share the same birthday, the database needs a way to tell them apart.

Student_ID (PK)	First_Name	Last_name	Email
101	Alice	Smith	alice.s@email.com
102	Bob	Miller	bob.m@email.com
103	Alice	Smith	asmith99@email.com

Why Student_ID is the Primary Key:
Uniqueness: Alice #101 and Alice #103 have different IDs. If Alice #101 drops a class, the system won't accidentally remove Alice #103.
Non-Null: Every student must have an ID to be enrolled in the system.
Efficiency: When a professor enters a grade, they link it to 101, not the name "Alice," which is too common.

Other Real-World Examples:
E-commerce: Order_Number (e.g., #88291-X)
Inventory: SKU or Barcode
Social Media: Username (though many systems use a hidden User_ID number behind the scenes)

4. Explain what a database schema is. Describe what information a schema defines and why schemas are important for maintaining consistent data structure.

Ans:-
A database schema is the formal blueprint or "architectural plan" of your database. It defines the organization of data and the rules that govern it before any actual information is even added. 
What a Schema Defines
Think of it as a set of instructions that tells the database engine exactly how to behave:
Structure: Which tables exist and how they relate to one another (the "map").
Attributes: The specific columns in each table and their data types (e.g., "Age" must be an integer, "Name" must be text).
Constraints: The "guardrails," such as which columns are Primary Keys, which cannot be empty (Not Null), and which must be unique.
Relationships: How tables connect via Foreign Keys (e.g., "Every Order must belong to an existing Customer"). 
Why Schemas are Essential
Without a schema, a database is just a messy pile of files. Schemas provide: 
Data Integrity: They act as a filter. If a system tries to save a word where a price (number) should be, the schema rejects it, preventing "garbage" data from breaking your AI models.
Consistency: Every record in a table follows the exact same format. This allows your code to reliably ask for "Email" and know it will always find a string in that specific spot.
Performance: The database uses the schema to create Indexes, which are like a book's index, allowing it to find specific data points in milliseconds instead of scanning the entire drive. 

5. Explain how relationships between tables work in relational databases. Describe the role of foreign keys and how tables such as users and orders can be connected

Ans:-
In a relational database, relationships allow you to split data into logical "buckets" (tables) while still being able to pull them together when needed. This is done using Foreign Keys. 
How Foreign Keys Work
A Foreign Key (FK) is a column in one table that points to the Primary Key (PK) of another table. It acts like a "link" or a "pointer." Instead of copying all of a user's information into an order, you just store the user’s unique ID. 
Example: Users and Orders
Imagine a simple e-commerce setup.
Users Table (The "Parent")
User_ID (PK)	Name	Email
1	Alice	alice@email.com
2	Bob	bob@email.com
Orders Table (The "Child")
Order_ID (PK)	User_ID (FK)	Product	Total
101	1	Laptop	₹80,000
102	2	Mouse	₹1,500
103	1	Keyboard	₹3,000
The Role of the Foreign Key
Identity Mapping: The User_ID in the Orders table tells the database exactly who bought the product.
Data Integrity (Referential Integrity): The database will prevent you from creating an order for User_ID: 99 if that user doesn't exist in the Users table. It keeps the data "honest."
Efficiency: To find all orders for Alice, the database just searches for User_ID: 1 in the Orders table. It doesn't have to deal with her name or email until you actually need to print a receipt. 
Types of Relationships
One-to-Many: One user can have many orders (the most common type).
Many-to-Many: One student can have many classes, and one class has many students (requires a "join table" in the middle).
One-to-One: One user has exactly one profile (usually for sensitive data like ID verification)