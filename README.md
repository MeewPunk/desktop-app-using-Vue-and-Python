Desktop App Using Vue and Python (webview)
This project combines the power of Vue.js for frontend development and Python for backend functionality, wrapped in a webview to create a desktop application. Below are the steps to set up and run the application.

Backend Setup
Navigate to the backend directory:
cd backend
Ensure you have Python 3.11.3 installed.

Windows
Activate the virtual environment:
```bash
env\Scripts\activate
```
macOS/Linux
Activate the virtual environment:
```bash
source env/bin/activate
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```
Run the backend server:
```bash
python main.py
```
Frontend Setup
Navigate to the frontend directory:
```bash
cd frontend
```
Install the required npm packages:
```bash
npm install
```
Development
To run the frontend in development mode:
```bash
npm run dev
```
Production
To build the frontend for production:
```bash
npm run build
```
After building, make the following changes:

Rename indexxxxxxxxxxxxxx.css to index.css and move it to backend/static/assets/.
Rename indexxxxxxxxxxxxxx.js to index.js and move it to backend/static/assets/.
Running the Application
After completing both backend and frontend setup, you can run the desktop application by starting the backend server and opening the webview interface.

Enjoy your Vue.js and Python powered desktop application!
