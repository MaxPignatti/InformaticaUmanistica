import React from 'react';
import { createRoot } from 'react-dom/client';
import AppComponent from 'app/app';

const rootEl = document.getElementById('root');
const root = createRoot(rootEl);

const render = Component =>
  root.render(
        <div>
          <Component />
        </div>
  );

render(AppComponent);
