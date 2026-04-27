import react, { Component, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

class App extends Component {
    state = { message: "" }
    func1 = (childData) => {
      this.setState({ message: childData });
    }
    render() {
      return (
        <div>
          <AppInner parentCallback =
            { this.func1 } />
          <p> { this.state.message } </p>
        </div>
      );
    }
}

class AppInner extends Component {
  sendData = () => {
    setInterval(() => {
      const currTime = Date();
      this.props.parentCallback(currTime);
    }, 1000);
  }
  componentDidMount() {
    this.sendData();
  }
  render() {
    return <div></div>
  }
}

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <SandboxComponent />
//    </>
//   )
// }

export default App
