import { useState } from "react";

const Boton = (props) => {
    const [mensaje, setMensaje] = useState("")


    return (<div className="container">
        <button className="btn btn-danger" onClick={props.sumar}>Presiona para decir hola</button>

    </div>);
}

export default Boton; 