function envia(){
    const nome = document.getElementById("nome").value
    const telefone = document.getElementById("telefone").value
    const email = document.getElementById("email").value

    const front = document.getElementById("front").checked ? "Frontend" : ""
    const back = document.getElementById("back").checked ? "Backend" : ""
    const full = document.getElementById("full").checked ? "Fullstack" : ""

    const java = document.getElementById("java").checked ? "Java " : ""
    const c = document.getElementById("c#").checked ? "C# " : ""
    const html = document.getElementById("html").checked ? "HTML " : ""
    const css = document.getElementById("css").checked ? "CSS " : ""
    const js = document.getElementById("js").checked ? "Javascript " : ""


    const alert =
            `Olá, ${nome}!
            Telefone = ${telefone}
            Email = ${email}
            Techs = ${java+c+html+css+js}
            Trilha = ${front+back+full}`;

            window.alert(alert);
    reseta()
}

function reseta(){
    document.getElementById("nome").value = ""
    document.getElementById("telefone").value = ""
    document.getElementById("email").value = ""
    document.getElementById("front").checked = false
    document.getElementById("back").checked = false
    document.getElementById("full").checked = false
    document.getElementById("java").checked = false
    document.getElementById("c#").checked = false
    document.getElementById("html").checked = false
    document.getElementById("css").checked = false
    document.getElementById("js").checked = false
}