import * as THREE from 'three';

const canvas = document.getElementById( { elementId: 'canvas' } );

// 1. Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color('#F0F0F0');

// 2. Camera
const camera = new THREE.PerspectiveCamera( { fov: 75, aspect: window.innerWidth / window.innerHeight, near: 0.1, far: 1000 } );
camera.position.z = 5;

// 3. Object
const geometry = new THREE.DodecahedronGeometry();
const material = new THREE.MeshBasicMaterial( { color: '#468585' } );
const dodecahedron = new THREE.Mesh(geometry, material);

const boxGeometry = new THREE.BoxGeometry( { width: 2, height: 0.1, depth: 2 } );
const boxMaterial = new THREE.MeshBasicMaterial( { color: '#B4B4B3' } );
const box = new THREE.Mesh(boxGeometry, boxMaterial);
box.position.y = -1.5;

scene.add(dodecahedron);
scene.add(box);

// 4. Light
const light = new THREE.SpotLight( { color: 0x006769, intensity: 100} );
light.position.set( { x: 1, y: 1, z: 1 } );
scene.add(light);

// 5. Renderer
const renderer = new THREE.WebGLRenderer( { parameters: canvas } );

renderer.setSize(window.innerWidth, window.innerHeight);

renderer.render(scene, camera);