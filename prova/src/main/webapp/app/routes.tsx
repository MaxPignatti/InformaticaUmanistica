import React, { useEffect } from 'react';
import { Route, useLocation } from 'react-router-dom';
import Home from 'app/modules/createPlaylist/createPlaylist';

const AppRoutes = () => {
  const location = useLocation();

  useEffect(() => {
    const hash = location.hash;
    const tokenParam = new URLSearchParams(hash.substring(1)).get('access_token');
    if (tokenParam) {
      sessionStorage.setItem('accessToken', tokenParam);
      window.location.href = '/';
    }
  }, [location]);

  return (
    <div className="view-routes">
      <Route index element={<Home />} />
      <Route path="/" element={<Home />} />
    </div>
  );
};

const App = () => {
  return (
    <AppRoutes />
  );
};

export default App;
