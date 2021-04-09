import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Register from "./components/Register";
import App from "./App";

const routing = (
  <Router>
    <Header />
    <Switch>
      <Route exact path="/" component={App} />
      <Route path="/register" component={Register} />
    </Switch>
    <Footer />
  </Router>
);

ReactDOM.render(routing, document.getElementById("root"));
