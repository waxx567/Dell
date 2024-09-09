import * as THREE from 'three';

// 1. Create the scene
const scene: THREE.scene = new THREE.scene();
scene.background = new THREE.Color('#F0F0F0');

// 2. Add the camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000); 
// For the Perspective Camera, 75 is the FOV, then comes the aspect ratio, then the near and far planes
camera.position.z = 5;

// 3. Create and add a cube object
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshLambertMaterial({ color: '#468585', emissive: '#468585' });

// 4. Add lighting

// 5. Set up the renderer

// 6. Animate the scene