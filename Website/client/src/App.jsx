import './App.css'
import { Route, Routes } from 'react-router-dom'
import AddEvent from './components/addEvent'
import AddUser from './components/addUser'
import AddSig from './components/addSig'
import Success from './components/success'


function App() {
  return (
    <Routes>
      <Route path="/addEvent" element={<AddEvent />} />
      <Route path="/addUser" element={<AddUser />} />
      <Route path="/addSig" element={<AddSig />} />
      <Route path="/success" element={<Success />} />
    </Routes>
  )
}

export default App