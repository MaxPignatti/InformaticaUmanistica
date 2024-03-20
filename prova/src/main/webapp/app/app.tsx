import "./app.css";
import React, { useState, useEffect } from "react";
import CreatePlaylistPage from "./modules/createPlaylist/createPlaylist";

function App() {
  const CLIENT_ID = "08d52968d40a4cb999ddd47d784b5ac5";
  const REDIRECT_URI = "http://localhost:3000";
  const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize";
  const RESPONSE_TYPE = "token";

  const [token, setToken] = useState("");

  useEffect(() => {
    const hash = window.location.hash;
    let token = window.sessionStorage.getItem("token");

    if (!token && hash) {
      token = hash
        .substring(1)
        .split("&")
        .find(elem => elem.startsWith("access_token"))
        .split("=")[1];

      window.location.hash = "";
      window.sessionStorage.setItem("token", token);
    }

    setToken(token);
  }, []);

  const logout = () => {
    setToken("");
    window.sessionStorage.clear();
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Spotify React</h1>
        {!token ? (
          <a
            href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}
          >
            Login to Spotify
          </a>
        ) : (
          <>
            <CreatePlaylistPage></CreatePlaylistPage>
            <button onClick={logout}>Logout</button>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
