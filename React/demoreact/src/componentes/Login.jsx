const Login = (props) => {
    return (<>  <h1 className="h3 mb-3 fw-normal">Please sign in</h1>
        <div className="form-floating">
            <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com" />
            <label for="floatingInput">Email address</label>
        </div>
        <br />
        <div className="form-floating">
            <input type="password" className="form-control" id="floatingPassword" placeholder="Password" />
            <label for="floatingPassword">Password</label>
        </div>
        <div className="form-check text-start my-3">
            <input className="form-check-input" type="checkbox" value="remember-me" id="checkDefault" />
            <label className="form-check-label" for="checkDefault">            recuerdame     </label>
        </div>
        <button className="btn btn-primary w-100 py-2" >Sign in</button>
        <p className="mt-5 mb-3 text-body-secondary">© 2017–2025</p>
        </>);
}

export default Login;