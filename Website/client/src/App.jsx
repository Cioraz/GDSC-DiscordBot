import './App.css'
import { Route, Routes } from 'react-router-dom'
import AddEvent from './components/addEvent'
import AddUser from './components/addUser'


function App() {
  return (
    <Routes>
      <Route path="/addEvent" element={<AddEvent />} />
      <Route path="/addUser" element={<AddUser />} />
    </Routes>
  )

}

export default App