import './css/login.css'
// import banner3 from './assets/banner3.png'
function Login  () { 

    return ( <section id="login">


        <div id="login-main">

            <div id="loginsup">
                <h2>Login</h2>
            </div>

            <div id="usuario">
                <input type="text" name="Usuario" placeholder="Usuário" id="login-usuario"/>
            </div>

            <div id="-senha">
                <input type="password" name="Senha" placeholder="Senha" id="login-senha"/>
            </div>

            <div id="logininf">
                <button class= "button_login"><p class="login">LOGIN</p></button>
            </div>

        </div>

    </section>
    );
};

export default Login;