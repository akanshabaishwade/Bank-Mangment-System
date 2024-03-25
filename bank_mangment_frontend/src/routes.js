// Routes.js
import React from 'react';
import { Switch, Route } from 'react-router';
import Home from './Home';
import About from './About';
import Dashboard from './Dashboard';

function Routes() {
  return (
    <Switch>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/dashboard">
        <Dashboard />
      </Route>
      <Route path="/">
        <Home />
      </Route>
    </Switch>
  );
}

export default Routes;
