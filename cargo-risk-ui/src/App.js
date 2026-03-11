import React,{useState} from "react"
import axios from "axios"
import "./App.css"
import {motion} from "framer-motion"

const ports=[
"Mumbai","Chennai","Kolkata","Singapore","Shanghai",
"Dubai","Hamburg","Rotterdam","Antwerp","Los Angeles",
"New York","Seattle","Houston","London","Barcelona",
"Santos","Sydney","Cape Town","Durban"
]

function App(){

const [source,setSource]=useState("")
const [destination,setDestination]=useState("")
const [weather,setWeather]=useState("")
const [congestion,setCongestion]=useState("")
const [cargo,setCargo]=useState("")
const [result,setResult]=useState(null)
const [animation,setAnimation]=useState(0)

const animations=[
{opacity:0,y:50},
{opacity:0,scale:0.5},
{opacity:0,x:-100},
{opacity:0,rotate:10}
]

const submit=async()=>{

try{

const res=await axios.post("http://localhost:5000/predict",{
source,
destination,
weather,
congestion,
cargo
})

setResult(res.data)

setAnimation(Math.floor(Math.random()*animations.length))

}catch(error){

alert("Backend connection failed")

}

}

return(

<div className="main">

<motion.div
className="card"
initial={{opacity:0,y:-50}}
animate={{opacity:1,y:0}}
transition={{duration:0.6}}

>

<h1>Cargo Risk Predictor</h1>

<select onChange={(e)=>setSource(e.target.value)}>

<option>Select Source Port</option>
{ports.map(p=>(
<option key={p}>{p}</option>
))}
</select>

<select onChange={(e)=>setDestination(e.target.value)}>

<option>Select Destination Port</option>
{ports.map(p=>(
<option key={p}>{p}</option>
))}
</select>

<input
placeholder="Weather Severity (1-5)"
onChange={(e)=>setWeather(e.target.value)}
/>

<input
placeholder="Port Congestion (1-5)"
onChange={(e)=>setCongestion(e.target.value)}
/>

<select onChange={(e)=>setCargo(e.target.value)}>

<option value="">Cargo Type</option>
<option value="normal">Normal</option>
<option value="fragile">Fragile</option>
</select>

<motion.button
whileHover={{scale:1.05}}
whileTap={{scale:0.9}}
onClick={submit}

>

Predict Risk
</motion.button>

</motion.div>

{result &&(

<motion.div
className="result"
initial={animations[animation]}
animate={{opacity:1,x:0,y:0,scale:1,rotate:0}}
transition={{duration:0.6}}

>

<h2>Prediction Result</h2>

<p>Distance: {result.distance.toFixed(2)} km</p>
<p>Weather Used: {result.weather}</p>
<p>Port Congestion: {result.congestion}</p>
<p>Cargo: {result.cargo}</p>

<h3>Risk Score: {result.risk_score}</h3>

<div className={`risk ${result.risk_level.replace(" ","-")}`}>
{result.risk_level}
</div>

</motion.div>

)}

</div>

)

}

export default App
