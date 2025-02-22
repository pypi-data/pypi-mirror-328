import os
import webbrowser
import time
from flask import Flask, request, render_template_string, redirect, url_for, session
from collections import OrderedDict
from . import db  
import uuid
from openai import OpenAI

# Built-in themes.
DEFAULT_THEMES = {
    "light": {
        "background": "#f4f7f9",
        "text_color": "#333",
        "nav_background": "#007acc",
        "nav_text": "#fff",
        "chat_background": "#eef2f7",
        "chat_border": "#e0e0e0",
        "widget_background": "#dddddd",
        "widget_border": "#007acc",
        "sidebar_background": "#eeeeee",
        "sidebar_text": "#333"
    },
    "dark": {
        "background": "#1e1e1e",
        "text_color": "#ccc",
        "nav_background": "#333",
        "nav_text": "#fff",
        "chat_background": "#2e2e2e",
        "chat_border": "#555",
        "widget_background": "#444",
        "widget_border": "#007acc",
        "sidebar_background": "#2a2a2a",
        "sidebar_text": "#ccc"
    }
}

ICON = "👀"

class SyntaxMUI:
    def __init__(self, title=ICON + "SMX UI", project_title=ICON + "SyntaxMatrix UI", host="127.0.0.1", port=5000, theme="light"):
        self.app = Flask(__name__)
        self.app.secret_key = "syntaxmatrix_secret"
        self.title = title
        self.host = host
        self.port = port
        self.project_title = project_title

        # Initialise DB and load pages.
        db.init_db()
        self.pages = db.get_pages()

        # Default UI mode: 'default', 'bubble', 'card', or 'deepseek'
        self.ui_mode = "deepseek"

        # Dictionary for main UI widgets.
        self.widgets = OrderedDict()

        # Set theme.
        if theme in DEFAULT_THEMES:
            self.theme = DEFAULT_THEMES[theme]
        elif isinstance(theme, dict):
            self.theme = theme
        else:
            self.theme = DEFAULT_THEMES["light"]

        self.theme_toggle_enabled = False

        self.setup_routes()

    def set_ui_mode(self, mode):
        if mode not in ["default", "card", "bubble", "deepseek"]:
            raise ValueError("UI mode must be one of: 'default', 'card', 'bubble', 'deepseek'.")
        self.ui_mode = mode

    def set_project_title(self, project_title):
        self.project_title = project_title

    def set_theme(self, theme):
        if theme in DEFAULT_THEMES:
            self.theme = DEFAULT_THEMES[theme]
        elif isinstance(theme, dict):
            self.theme = theme
        else:
            raise ValueError("Theme must be 'light', 'dark', or a custom dict.")

    def enable_theme_toggle(self):
        self.theme_toggle_enabled = True

    def columns(self, *components):
        col_html = "<div style='display:flex; gap:10px;'>"
        for comp in components:
            col_html += f"<div style='flex:1;'>{comp}</div>"
        col_html += "</div>"
        return col_html

    # Public API: Widget registration.
    def text_input(self, key, label, placeholder=""):
        if key not in self.widgets:
            self.widgets[key] = {"type": "text_input", "key": key, "label": label, "placeholder": placeholder}

    def button(self, key, label, callback=None):
        if key not in self.widgets:
            self.widgets[key] = {"type": "button", "key": key, "label": label, "callback": callback}

    def file_uploader(self, key, label, accept_multiple_files=False):
        if key not in self.widgets:
            self.widgets[key] = {"type": "file_upload", "key": key, "label": label, "accept_multiple": accept_multiple_files}

    def get_text_input_value(self, key, default=""):
        return session.get(key, default)

    def clear_text_input_value(self, key):
        session[key] = ""
        session.modified = True

    def get_file_upload_value(self, key):
        return session.get(key, None)

    def get_chat_history(self):
        return session.get("chat_history", [])

    def set_chat_history(self, history):
        session["chat_history"] = history
        session.modified = True

    def clear_chat_history(self):
        session["chat_history"] = []
        session.modified = True

    def write(self, content):
        if "content_buffer" not in session:
            session["content_buffer"] = ""
        session["content_buffer"] += str(content)
        session.modified = True

    def setup_routes(self):
        def head_html():
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
              <meta charset="UTF-8">
              <style>
                body {{
                  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                  background: {self.theme["background"]};
                  color: {self.theme["text_color"]};
                }}
                nav {{
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                  background: {self.theme["nav_background"]};
                  padding: 10px 20px;
                  position: fixed;
                  top: 0;
                  left: 0;
                  right: 0;
                  z-index: 1000;
                }}
                nav a {{
                  color: {self.theme["nav_text"]};
                  text-decoration: none;
                  margin-right: 15px;
                  font-size: 1.1em;
                }}
                #sidebar {{
                  position: fixed;
                  top: 60px;
                  left: -240px;
                  width: 240px;
                  height: calc(100% - 60px);
                  background: {self.theme["sidebar_background"]};
                  color: {self.theme["sidebar_text"]};
                  overflow-y: auto;
                  padding: 15px;
                  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
                  transition: left 0.3s ease;
                  z-index: 999;
                }}
                #sidebar.open {{
                  left: 0;
                }}
                #sidebar-toggle-btn {{
                  position: fixed;
                  top: 65px;
                  left: 10px;
                  z-index: 1100;
                  padding: 5px 10px;
                  background: {self.theme["nav_background"]};
                  color: {self.theme["nav_text"]};
                  border: none;
                  border-radius: 4px;
                  cursor: pointer;
                }}
                #chat-history {{
                  width: 100%;
                  max-width: 850px;
                  margin: 80px auto 25px auto;
                  padding: 10px;
                  background: {self.theme["chat_background"]};
                  border-radius: 8px;
                  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                  overflow-y: auto;
                  min-height: 350px;
                }}
                #widget-container {{
                  max-width: 850px;
                  margin: 0 auto 60px auto;
                }}
                {self._chat_css()}
              </style>
              <title>{self.title}</title>
            </head>
            <body>
            """

        @self.app.route("/", methods=["GET", "POST"])
        def home():
            # If this is a new session (first visit), initialize a fresh chat.
            if "initiated" not in session:
                session["past_sessions"] = []
                session["current_session"] = {"id": str(uuid.uuid4()), "title": "Nuveaux", "history": []}
                session["chat_history"] = []
                session["initiated"] = True

            if request.method == "POST":
                for key, widget in self.widgets.items():
                    if widget["type"] == "text_input":
                        session[key] = request.form.get(key, widget.get("placeholder", ""))
                    elif widget["type"] == "file_upload":
                        if key in request.files:
                            file_obj = request.files[key]
                            try:
                                content = file_obj.read().decode("utf-8", errors="replace")
                            except Exception:
                                content = "<binary data>"
                            session[key] = {"filename": file_obj.filename, "content": content}
                    elif widget["type"] == "button":
                        if key in request.form and widget.get("callback"):
                            widget["callback"]()

                action = request.form.get("action")
                if action == "update_session":
                    sess_id = request.form.get("session_id")
                    new_title = request.form.get("session_title", "").strip()
                    past = session.get("past_sessions", [])
                    for s in past:
                        if s["id"] == sess_id:
                            s["title"] = new_title if new_title else s["title"]
                    session["past_sessions"] = past
                    session.modified = True
                elif action == "set_session":
                    sess_id = request.form.get("session_id")
                    past = session.get("past_sessions", [])
                    selected = None
                    for s in past:
                        if s["id"] == sess_id:
                            selected = s
                            break
                    if selected:
                        session["current_session"] = selected
                        session["chat_history"] = selected.get("history", [])
                        session.modified = True
                elif action == "new_session":
                    current = session.get("current_session", {"history": []})
                    if not isinstance(current, dict):
                        current = {"id": str(uuid.uuid4()), "title": "New chat", "history": []}
                    current["history"] = session.get("chat_history", [])
                    # Generate a contextual title based on the full discussion.
                    contextual_title = SyntaxMUI.generate_contextual_title(current["history"])
                    current["title"] = contextual_title if contextual_title not in ["Empty Chat", ""] else "New chat"
                    if current["history"]:
                        past = session.get("past_sessions", [])
                        past.append(current)
                        session["past_sessions"] = past
                        session.modified = True
                    # Start a new virgin session.
                    session["current_session"] = {"id": str(uuid.uuid4()), "title": "Nuveaux", "history": []}
                    session["chat_history"] = []
                if "clear_chat" in request.form:
                    self.clear_chat_history()

                return redirect(url_for("home"))

            current = session.get("current_session")
            if not isinstance(current, dict):
                current = {"id": str(uuid.uuid4()), "title": "Nuveaux", "history": []}
            current["history"] = session.get("chat_history", [])
            session["current_session"] = current

            nav_html = self._generate_nav()
            chat_html = self._render_chat_history()
            widget_html = self._render_widgets()
            sidebar_html = self._render_session_sidebar()

            scroll_and_toggle_js = """
            <script>
              window.onload = function() {
                var chatContainer = document.getElementById("chat-history");
                if(chatContainer) {
                  chatContainer.scrollTop = chatContainer.scrollHeight - 100;
                }
                var queryInput = document.querySelector('textarea[name="user_query"]');
                if(queryInput) { queryInput.focus(); }
              };
              const sidebarToggleBtn = document.getElementById("sidebar-toggle-btn");
              const sidebar = document.getElementById("sidebar");
              sidebarToggleBtn.addEventListener("click", function() {
                  sidebar.classList.toggle("open");
                  if(sidebar.classList.contains("open")){
                      sidebarToggleBtn.innerText = "X";
                  } else {
                      sidebarToggleBtn.innerText = "Sessions";
                  }
              });
            </script>
            """

            page_html = f"""
            {head_html()}
            {nav_html}
            <button id="sidebar-toggle-btn">>></button>
            {sidebar_html}
            <div style="margin:80px 10px 0 10px;">
              <div id="chat-history">{chat_html}</div>
              <div id="widget-container">{widget_html}</div>
            </div>
            {scroll_and_toggle_js}
            </body>
            </html>
            """
            return render_template_string(page_html)

        @self.app.route("/page/<page_name>")
        def view_page(page_name):
            nav_html = self._generate_nav()
            if page_name in self.pages:
                content = self.pages[page_name]
            else:
                content = f"No content found for page '{page_name}'."
            view_page_html = f"""
            {head_html()}
            {nav_html}
            <h1 style='text-align:center;'>{ICON}{page_name}</h1>
            <div style='max-width:800px;margin:20px auto;padding:20px;background:#fff;border-radius:8px;'>
              {content}
            </div>
            <div><a class='button' href='/'>Return to Home</a></div>
            </body>
            </html>
            """
            return render_template_string(view_page_html)

        @self.app.route("/admin", methods=["GET", "POST"])
        def admin_panel():
            if request.method == "POST":
                action = request.form.get("action")
                if action == "upload_files":
                    files = request.files.getlist("upload_files")
                    upload_folder = os.path.join(os.getcwd(), "uploads")
                    if not os.path.exists(upload_folder):
                        os.makedirs(upload_folder)
                    for file in files:
                        if file and file.filename.lower().endswith(".pdf"):
                            filepath = os.path.join(upload_folder, file.filename)
                            file.save(filepath)
                    session["upload_msg"] = "File(s) uploaded successfully!"
                elif action == "add_page":
                    page_name = request.form.get("page_name", "").strip()
                    page_content = request.form.get("page_content", "").strip()
                    if page_name and page_name not in self.pages:
                        db.add_page(page_name, page_content)
                elif action == "update_page":
                    old_name = request.form.get("old_name", "").strip()
                    new_name = request.form.get("new_name", "").strip()
                    new_content = request.form.get("new_content", "").strip()
                    if old_name in self.pages and new_name:
                        db.update_page(old_name, new_name, new_content)
                elif action == "delete_page":
                    del_page = request.form.get("delete_page", "").strip()
                    if del_page in self.pages:
                        db.delete_page(del_page)
                return redirect(url_for("admin_panel"))
            self.pages = db.get_pages()
            upload_msg = session.pop("upload_msg", "")
            alert_script = f"<script>alert('{upload_msg}');</script>" if upload_msg else ""
            return render_template_string(f"""
            <!DOCTYPE html>
            <html>
            <head>
              <title>{ICON}Admin Panel</title>
              <style>
                body {{
                  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                  background: #f4f7f9;
                  padding: 20px;
                }}
                form {{
                  margin-bottom: 20px;
                  background: #fff;
                  padding: 15px;
                  border-radius: 8px;
                  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                input, textarea, select {{
                  padding: 10px;
                  font-size: 1em;
                  margin: 5px 0;
                  width: 100%;
                  border: 1px solid #ccc;
                  border-radius: 4px;
                }}
                button {{
                  padding: 10px 20px;
                  font-size: 1em;
                  background: #007acc;
                  color: #fff;
                  border: none;
                  border-radius: 4px;
                  cursor: pointer;
                }}
                button:hover {{
                  background: #005fa3;
                }}
              </style>
            </head>
            <body>
              <h1>Admin Panel</h1>
              {alert_script}
              <h3>Upload PDF Files</h3>
              <form method="post" enctype="multipart/form-data">
                <input type="file" name="upload_files" accept=".pdf" multiple>
                <button type="submit" name="action" value="upload_files">Upload</button>
              </form>
              <form method="post">
                <h3>Add a Page</h3>
                <input type="text" name="page_name" placeholder="Page Name" required>
                <textarea name="page_content" placeholder="Page Content"></textarea>
                <button type="submit" name="action" value="add_page">Add Page</button>
              </form>
              <form method="post">
                <h3>Update an Existing Page</h3>
                <select name="old_name">
                  {''.join(f'<option value="{{p}}">{{p}}</option>' for p in self.pages)}
                </select>
                <input type="text" name="new_name" placeholder="New Page Name" required>
                <textarea name="new_content" placeholder="New Page Content"></textarea>
                <button type="submit" name="action" value="update_page">Update Page</button>
              </form>
              <form method="post">
                <h3>Delete a Page</h3>
                <select name="delete_page">
                  {''.join(f'<option value="{{p}}">{{p}}</option>' for p in self.pages)}
                </select>
                <button type="submit" name="action" value="delete_page">Delete Page</button>
              </form>
              <p><a href="/">Return to Home</a></p>
            </body>
            </html>
            """)

        @self.app.route("/toggle_theme", methods=["GET"])
        def toggle_theme():
            current = session.get("theme", "light")
            new_theme = "dark" if current == "light" else "light"
            session["theme"] = new_theme
            self.set_theme(new_theme)
            return redirect(url_for("home"))

        @self.app.route("/rename_session", methods=["POST"])
        def rename_session():
            sess_id = request.form.get("session_id")
            new_title = request.form.get("new_title", "").strip()
            past = session.get("past_sessions", [])
            for s in past:
                if s["id"] == sess_id:
                    s["title"] = new_title if new_title else s["title"]
            session["past_sessions"] = past
            session.modified = True
            return "OK", 200

        @self.app.route("/delete_session", methods=["POST"])
        def delete_session():
            sess_id = request.form.get("session_id")
            past = session.get("past_sessions", [])
            past = [s for s in past if s["id"] != sess_id]
            session["past_sessions"] = past
            session.modified = True
            return "OK", 200

    def _generate_nav(self):
        left_items = [f'<a href="/">{ICON}SMX</a>']
        for page in self.pages:
            left_items.append(f'<a href="/page/{page}">{page}</a>')
        left_items.append(f'<a href="/admin">Admin</a>')
        left_html = "".join(left_items)
        right_html = ""
        if self.theme_toggle_enabled:
            right_html = f'<a href="/toggle_theme">Theme</a>'
        return f"""
        <nav>
          <div>{left_html}</div>
          <div>{right_html}</div>
        </nav>
        """

    def _render_chat_history(self):
        messages = session.get("chat_history", [])
        chat_html = ""
        if not messages:
            chat_html += f"""
            <div id="deepseek-header" style="text-align:center; margin-top:40px; margin-bottom:20px;">
              <h1>{self.project_title}.</h1>
              <p>How can I help you today?</p>
            </div>
            """
        if messages:
            for role, message in messages:
                timestamp = ""
                if self.ui_mode == "card":
                    timestamp = f"""<span style="float: right; font-size: 0.8em; color: {self.theme['text_color']};">{time.strftime('%H:%M')}</span>"""
                chat_html += f"""
                <div class='chat-message {role.lower()}'>
                  <strong>{role.capitalize()}</strong>{timestamp}
                  <p>{message}</p>
                </div>
                """
        return chat_html

    def _render_widgets(self):
        if self.ui_mode == "default":
            widget_html = f"""
            <form method="POST" style="max-width:800px; margin:0 auto; padding:12px; background:lightgray; border:1px solid black; border-radius:4px; margin-bottom:60px;">
              <div style='margin-bottom:10px;'>
                <textarea name="user_query" rows="1" placeholder="Enter your RAG query" style="width: calc(100% - 20px); padding:12px; font-size:1em; border:1px solid #ccc; border-radius:4px;" autofocus onkeydown="if(event.key==='Enter' && !event.shiftKey){{event.preventDefault(); this.form.querySelector('button[name=\\'submit_query\\']').click();}}">{session.get('user_query', '')}</textarea>
              </div>
              <div style="text-align:center;">
                <button type="submit" name="submit_query" value="clicked" style="padding:10px 20px; margin-right:10px; border:none; border-radius:20px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Send</button>
                <button type="submit" name="clear_chat" value="clicked" style="padding:10px 20px; border:none; border-radius:20px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Clear</button>
              </div>
            </form>
            """
        elif self.ui_mode == "bubble":
            widget_html = f"""
            <form method="POST" style="max-width:800px; margin:0 auto; display:flex; align-items:center; justify-content:center; padding:12px; background:{self.theme['nav_background']}; border:1px solid red; margin-bottom:60px;">
              <div style="flex:1; min-width:200px; margin:10px; padding:0 10px;">
                <textarea name="user_query" rows="1" placeholder="Enter query" style="width: calc(100% - 20px); padding:12px; font-size:1em; border:1px solid #ccc; border-radius:50px;" autofocus onkeydown="if(event.key==='Enter' && !event.shiftKey){{event.preventDefault(); this.form.querySelector('button[name=\\'submit_query\\']').click();}}">{session.get('user_query', '')}</textarea>
              </div>
              <button type="submit" name="submit_query" value="clicked" style="padding:10px 20px; margin-right:10px; border:none; border-radius:20px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Send</button>
              <button type="submit" name="clear_chat" value="clicked" style="padding:10px 20px; border:none; border-radius:20px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Clear</button>
            </form>
            """
        elif self.ui_mode == "card":
            widget_html = f"""
            <form method="POST" style="max-width:800px; margin:0 auto; background:#fff; padding:12px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1); margin-bottom:60px;">
              <div style="margin-bottom:10px;">
                <textarea name="user_query" rows="1" placeholder="Type your query here..." style="width: calc(100% - 20px); padding:12px; font-size:1em; border:1px solid #ccc; border-radius:10px;" autofocus onkeydown="if(event.key==='Enter' && !event.shiftKey){{event.preventDefault(); this.form.querySelector('button[name=\\'submit_query\\']').click();}}">{session.get('user_query', '')}</textarea>
              </div>
              <div style="text-align:right;">
                <button type="submit" name="submit_query" value="clicked" style="padding:10px 20px; margin-right:10px; border:none; border-radius:4px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Send</button>
                <button type="submit" name="clear_chat" value="clicked" style="padding:10px 20px; border:none; border-radius:4px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Clear</button>
              </div>
            </form>
            """
        elif self.ui_mode == "deepseek":
            widget_html = f"""
            <form method="POST" style="max-width:800px; margin:30px auto; padding:0 10px;">
              <div style="display:flex; gap:10px; align-items:center;">
                <textarea name="user_query" rows="3" placeholder="Message DeepSeek" style="flex:1; min-width:200px; padding:12px; font-size:1em; border:1px solid #ccc; border-radius:4px;" autofocus onkeydown="if(event.key==='Enter' && !event.shiftKey){{event.preventDefault(); this.form.querySelector('button[name=\\'submit_query\\']').click();}}"></textarea>
                <button type="submit" name="submit_query" value="clicked" style="padding:10px 20px; border:none; border-radius:4px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Send</button>
                <button type="submit" name="clear_chat" value="clicked" style="padding:10px 20px; border:none; border-radius:4px; background:{self.theme['nav_background']}; color:{self.theme['nav_text']}; cursor:pointer;">Clear</button>
              </div>
            </form>
            """
        else:
            widget_html = "<div>No valid UI mode selected.</div>"
        return widget_html

    def _render_session_sidebar(self):
        current = session.get("current_session", {"title": "Nuveaux"})
        past_sessions = session.get("past_sessions", [])
        sidebar_content = f"""
        <div id="sidebar">
            <div style="padding: 10px; background: {self.theme['nav_background']}; color: {self.theme['nav_text']};">
                <button type="button" onclick="createNewChat()">New chat</button>
            </div>
            <h3 style="margin:10px 0 5px 10px;">Current Session</h3>
            <ul style="list-style-type: none; padding: 0 10px;">
                <li style="margin-bottom: 10px; padding: 5px; background: #cce5ff;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span>{current.get("title", "Nuveaux")}</span>
                    </div>
                </li>
            </ul>
        """
        if past_sessions:
            sidebar_content += f"""<h3 style="margin:10px 0 5px 10px;">Past Sessions</h3>
            <ul style="list-style-type: none; padding: 0 10px;">"""
            for s in past_sessions:
                sidebar_content += f"""
                <li style="margin-bottom: 10px; padding: 5px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span onclick="setSession('{s['id']}')" style="cursor: pointer;">{s['title']}</span>
                        <span>
                            <button type="button" onclick="renameSessionPrompt('{s['id']}', '{s['title']}')" style="background: none; border: none; color: {self.theme['sidebar_text']};">...</button>
                            <button type="button" onclick="deleteSession('{s['id']}')" style="background: none; border: none; color: {self.theme['sidebar_text']};">X</button>
                        </span>
                    </div>
                </li>
                """
            sidebar_content += "</ul>"
        else:
            sidebar_content += "<!-- No past sessions -->"
        sidebar_content += "</div>"
        js_functions = """
        <script>
        function createNewChat() {
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'action=new_session'
            }).then(response => response.text()).then(result => window.location.reload());
        }
        function setSession(sessionId) {
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'action=set_session&session_id=' + sessionId
            }).then(response => response.text()).then(result => window.location.reload());
        }
        function renameSessionPrompt(sessionId, currentTitle) {
            let newTitle = prompt('Enter new title for the session:', currentTitle);
            if (newTitle) {
                fetch('/rename_session', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'session_id=' + sessionId + '&new_title=' + encodeURIComponent(newTitle)
                }).then(response => response.text()).then(result => window.location.reload());
            }
        }
        function deleteSession(sessionId) {
            if (confirm('Are you sure you want to delete this session?')) {
                fetch('/delete_session', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'session_id=' + sessionId
                }).then(response => response.text()).then(result => window.location.reload());
            }
        }
        </script>
        """
        return sidebar_content + js_functions

    def _chat_css(self):
        if self.ui_mode == "bubble":
            return f"""
            .chat-message {{
              position: relative;
              max-width: 70%;
              margin: 10px 0;
              padding: 12px 18px;
              border-radius: 20px;
              animation: fadeIn 0.9s forwards;
              clear: both;
            }}
            .chat-message.user {{
              background: #dcf8c6;
              float: right;
              margin-right: 15px;
              border-bottom-right-radius: 2px;
            }}
            .chat-message.user::after {{
              content: '';
              position: absolute;
              right: -8px;
              top: 12px;
              width: 0;
              height: 0;
              border: 8px solid transparent;
              border-left-color: #dcf8c6;
              border-right: 0;
            }}
            .chat-message.bot {{
              background: #ffffff;
              float: left;
              margin-left: 15px;
              border-bottom-left-radius: 2px;
              border: 1px solid {self.theme['chat_border']};
            }}
            .chat-message.bot::before {{
              content: '';
              position: absolute;
              left: -8px;
              top: 12px;
              width: 0;
              height: 0;
              border: 8px solid transparent;
              border-right-color: #ffffff;
              border-left: 0;
            }}
            .chat-message p {{
              margin: 0;
              padding: 0;
              word-wrap: break-word;
            }}
            """
        elif self.ui_mode == "card":
            return f"""
            .chat-message {{
              display: block;
              margin: 15px 0;
              padding: 18px 22px;
              border-radius: 12px;
              animation: fadeIn 0.9s forwards;
              box-shadow: 0 2px 8px rgba(0,0,0,0.1);
              max-width: 80%;
              position: relative;
            }}
            .chat-message.user {{
              background: {self.theme['chat_background']};
              margin-left: auto;
              border: 1px solid {self.theme['chat_border']};
              border-right: 4px solid {self.theme['nav_background']};
            }}
            .chat-message.bot {{
              background: {self.theme['chat_background']};
              border: 1px solid {self.theme['chat_border']};
              border-left: 4px solid {self.theme['nav_background']};
            }}
            .chat-message p {{
              margin: 0;
              font-size: 0.95em;
              line-height: 1;
            }}
            .chat-message strong {{
              display: block;
              margin-bottom: 8px;
              color: {self.theme['nav_background']};
              font-size: 0.9em;
            }}
            """
        elif self.ui_mode == "deepseek":
            return f"""
            .chat-message {{
              display: block;
              margin: 10px auto;
              padding: 12px 18px;
              border-radius: 8px;
              animation: fadeIn 0.8s forwards;
              max-width: 80%;
              background: #fff;
              border: 1px solid {self.theme["chat_border"]};
            }}
            .chat-message.user {{
              background: #f1fdfa;
              border-color: #9ee9d8;
            }}
            .chat-message.bot {{
              background: #ffffff;
            }}
            .chat-message p {{
              margin: 0;
              word-wrap: break-word;
            }}
            #deepseek-header {{
              text-align: center;
              margin-top: 40px;
              margin-bottom: 20px;
            }}
            #deepseek-header h1 {{
              font-size: 2.2em;
              color: #444;
              margin: 0 0 10px 0;
            }}
            #deepseek-header p {{
              font-size: 1.1em;
              color: #666;
              margin: 0;
            }}
            """
        else:
            return f"""
            .chat-message {{
              display: block;
              width: 90%;
              margin-bottom: 10px;
              padding: 12px 18px;
              border-radius: 8px;
              animation: fadeIn 0.9s forwards;
            }}
            .chat-message.user {{
              background: #e1f5fe;
              text-align: right;
              margin-left: auto;
              max-width: 50%;
            }}
            .chat-message.bot {{
              background: #ffffff;
              border: 1px solid {self.theme["chat_border"]};
              text-align: left;
              max-width: 80%;
            }}
            """

    @staticmethod
    def generate_contextual_title(history):

        def generate_title(conversation_text):
            OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            llm = OpenAI(api_key=OPENAI_API_KEY)

            prompt =[
                {
                    "role": "system",
                    "content": "You are a title generation assistant"
                },
                {
                    "role": "user",
                    "content": "Generate a 5-word title that encompasses the discussion in the conversation."
                },
                {
                    "role": "assistant",
                    "content": f"Conversation: {conversation_text}\n\n"
                }
            ]

            try:
                response = llm.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=prompt,
                    temperature=0.3,
                    max_tokens=300
                )
                title = response.choices[0].message.content.strip()
            except Exception as e:
                title = f"Error: {str(e)}"
            return title 

        if not history:
            return "Empty Chat"
                
        # Convert the chat history into a single text block
        conversation_text = " ".join([f"{role}: {msg}" for role, msg in history if msg.strip()])
        # Call an external summarization function/model to generate a title.
        title = generate_title(conversation_text)
        return title

    def run(self):
        url = f"http://{self.host}:{self.port}/"
        webbrowser.open(url)
        self.app.run(host=self.host, port=self.port, debug=False)
