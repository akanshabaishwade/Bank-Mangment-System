import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from '/home/akansha/Bank Mangment System/bank_mangment_frontend/src/pages/home.js';
import About from '/home/akansha/Bank Mangment System/bank_mangment_frontend/src/pages/about.js';
// import Dashboard from './dashboard';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
                {/* <Route path="/dashboard" component={Dashboard} /> */}
            </Switch>
        </Router>
    );
};

export default App;
