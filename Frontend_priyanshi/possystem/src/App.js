import Home from "./pages/home/Home"
import Login from "./pages/login/Login"
import New from "./pages/new/New"
import Single from "./pages/single/Single"
import List from "./pages/list/List"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Routes,
  Link,
  BrowserRouter
} from "react-router-dom";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/">
           <Route index element={<Home/>}/>
           <Route path="login" element={<Login/>}/>
           <Route path="customer">
              <Route index element={<List/>}/>
              <Route path=":c_id" element={<Single/>}/>
              <Route path="new" element={<New/>}/>
           </Route>
           <Route path="products">
              <Route index element={<List/>}/>
              <Route path=":item_sku" element={<Single/>}/>
              <Route path="new" element={<New/>}/>
            </Route>
           </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
