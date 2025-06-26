import { useState } from 'react'
import Boton from './componentes/Boton'
import Login from './componentes/Login'

import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const sumar = () => {
    setCount(count + 1)
  }

  return (
    <div className='container'>
      <Boton sumar={sumar} />
      <Login  sumar={sumar} count={count}/>
      <p>{count}</p>



    </div>
  )
}

export default App
