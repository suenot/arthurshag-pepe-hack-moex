import React from 'react';
import {Route, Routes, useLocation, useNavigate} from 'react-router-dom';
import './App.css';
import AuthWrapper from "./components/Auth/AuthWrapper";
import Main from "./components/Main/Main";
import Preview from "./components/Preview/Preview";
import Layout from "./components/Layout/Layout";

function App() {
    const navigate = useNavigate();
    const location = useLocation().pathname;
  return (
      <Routes>
          <Route path="/auth" element={<AuthWrapper />}/>
          <Route path="/*" element={<Layout/>} />
          {/*<Route path="/preview" element={<Preview />}/>*/}
      </Routes>
  );
}

export default App;
