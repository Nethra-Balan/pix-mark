async function embed(){

    let form = new FormData()

    form.append("original",
        document.getElementById("original").files[0])

    form.append("logo",
        document.getElementById("logo").files[0])

    let res = await fetch("http://localhost:5000/phase1",{
        method:"POST",
        body:form
    })

    let data = await res.json()

    document.getElementById("embed_result").innerHTML = `

    <h3>Results</h3>

    <p>Watermarked Image</p>
    
    <a href="http://localhost:5000${data.watermarked}" download>
    Download
    </a>

    <p>Owner Share</p>
    
    <a href="http://localhost:5000${data.owner_share}" download>
    Download
    </a>

    `
}



async function verify(){

    let form = new FormData()

    form.append("suspect",
        document.getElementById("suspect").files[0])

    form.append("owner_share",
        document.getElementById("owner").files[0])

    form.append("logo",
        document.getElementById("logo_verify").files[0])

    let res = await fetch("http://localhost:5000/phase2",{
        method:"POST",
        body:form
    })

    let data = await res.json()

    document.getElementById("verify_result").innerHTML = `

    <h3>Verification Result</h3>

    <p><b>Status:</b> ${data.result}</p>

    <p><b>Similarity Score:</b> ${data.similarity}%</p>

    <p>Recovered Watermark</p>
    


    <a href="http://localhost:5000${data.recovered_logo}" download>
    Download Recovered Logo
    </a>

    `
}