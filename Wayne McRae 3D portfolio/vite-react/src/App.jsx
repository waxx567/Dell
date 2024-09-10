import {Canvas} from "@react-three/fiber";
import {OrbitControls} from "@react-three/drei";

const App = () => {
  return (
    <Canvas style={{ height: '100vh', width: '100vw', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <OrbitControls enableZoom={true} enablePan enableRotate />
    </Canvas>
  )
}

export default App;