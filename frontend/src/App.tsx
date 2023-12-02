import React from 'react';
import {Route, Routes, useLocation, useNavigate} from 'react-router-dom';
import './App.css';
import AuthWrapper from "./components/Auth/AuthWrapper";
import Main from "./components/Main/Main";
import Preview from "./components/Preview/Preview";

function App() {
    const navigate = useNavigate();
    const location = useLocation().pathname;
  return (
      <Routes>
          <Route path="/" element={<Main/>}>
              {/*<Route path="events">*/}
              {/*    <Route path="my" element={<EventList />} />*/}
              {/*    <Route path="map" element={<EventMap />} />*/}
              {/*    <Route index element={<EventList />} />*/}
              {/*</Route>*/}
              {/*<Route path="event">*/}
              {/*    <Route path=":eventId" element={<EventPage />} />*/}
              {/*    <Route path=":eventId/edit" element={<EventMaker />} />*/}
              {/*    <Route path=":eventId/invite/:key" element={<Invite />} />*/}
              {/*</Route>*/}
              {/*<Route path="profile" element={<Profile />} />*/}
          </Route>
          <Route path="/auth" element={<AuthWrapper />}/>
          {/*<Route path="/preview" element={<Preview />}/>*/}
      </Routes>
  );
}

export default App;
