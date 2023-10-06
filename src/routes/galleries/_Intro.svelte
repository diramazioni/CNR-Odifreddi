<script lang="ts">
import { Code, Notes, RevealJsContext, Slide } from '$lib';

import Galery from "$lib/Gallery.svelte";
const imageModules = import.meta.glob("$lib/assets/1-1/*.jpg"); 
const imagePath = Object.keys(imageModules).map((key) => imageModules[key].name);	
const interval = 1500;
</script>
<Slide>
  <Slide>
    <Galery {interval} imagePath={imagePath} />
  </Slide>
  <Slide>
    <p>ChatGPT</p>
    <h5>Can you make an svg animation of a stylized man walking?</h5>
  <svg width="200px" height="300px" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <!-- Add your SVG shapes representing the man here -->
    <rect x="90" y="190" width="20" height="40" fill="#336699"/>
    <circle cx="100" cy="170" r="10" fill="#FFCC66"/>
    <line x1="100" y1="180" x2="100" y2="200" stroke="white" stroke-width="2"/>
    <line x1="90" y1="210" x2="100" y2="200" stroke="white" stroke-width="2"/>
    <line x1="110" y1="210" x2="100" y2="200" stroke="white" stroke-width="2"/>
    <line x1="90" y1="230" x2="100" y2="220" stroke="white" stroke-width="2"/>
    <line x1="110" y1="230" x2="100" y2="220" stroke="white" stroke-width="2"/>
  
    <!-- Add animation keyframes -->
    <animateTransform
      attributeType="XML"
      attributeName="transform"
      type="translate"
      values="0 0; 50 0; 100 0; 150 0; 200 0;"
      dur="4s"
      repeatCount="indefinite"
    />
  </svg>
</Slide>
  <Slide>
    <p>cool, however I would move the leg and remove the blue rectangle</p>
    <svg width="200px" height="300px" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <!-- Add your SVG shapes representing the man here -->
      <!-- Body -->
      <circle cx="100" cy="150" r="20" fill="#336699"/>
      
      <!-- Head -->
      <circle cx="100" cy="120" r="10" fill="#FFCC66"/>
      
      <!-- Legs -->
      <!-- Left Leg -->
      <line x1="100" y1="170" x2="90" y2="190" stroke="white" stroke-width="2">
        <animate attributeName="y1" values="170;180;170;" dur="1s" repeatCount="indefinite" />
        <animate attributeName="y2" values="190;200;190;" dur="1s" repeatCount="indefinite" />
      </line>
      
      <!-- Right Leg -->
      <line x1="100" y1="170" x2="110" y2="190" stroke="white" stroke-width="2">
        <animate attributeName="y1" values="170;180;170;" dur="1s" begin="0.5s" repeatCount="indefinite" />
        <animate attributeName="y2" values="190;200;190;" dur="1s" begin="0.5s" repeatCount="indefinite" />
      </line>
    
      <!-- Add animation keyframes for walking -->
      <animateTransform
        attributeType="XML"
        attributeName="transform"
        type="translate"
        values="0 0; 30 0; 60 0; 90 0; 120 0;"
        dur="2s"
        repeatCount="indefinite"
      />
    </svg>
    
  </Slide>  
  <Slide>
    <p>the body as a line, add alternating arms, make the leg swing</p>
  <svg width="200px" height="300px" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <!-- Add your SVG shapes representing the man here -->
    <!-- Body as a line -->
    <line x1="100" y1="130" x2="100" y2="170" stroke="white" stroke-width="6">
      <animate attributeName="y1" values="130;140;130;" dur="1s" repeatCount="indefinite" />
      <animate attributeName="y2" values="170;160;170;" dur="1s" repeatCount="indefinite" />
    </line>
    
    <!-- Head -->
    <circle cx="100" cy="120" r="10" fill="white"/>
    
    <!-- Legs -->
    <!-- Left Leg -->
    <line x1="100" y1="170" x2="85" y2="200" stroke="white" stroke-width="4">
      <animate attributeName="y1" values="170;190;170;" dur="0.7s" repeatCount="indefinite" />
      <animate attributeName="y2" values="200;220;200;" dur="0.7s" repeatCount="indefinite" />
    </line>
    
    <!-- Right Leg -->
    <line x1="100" y1="170" x2="115" y2="200" stroke="white" stroke-width="4">
      <animate attributeName="y1" values="170;190;170;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
      <animate attributeName="y2" values="200;220;200;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
    </line>
    
    <!-- Arms -->
    <!-- Left Arm -->
    <line x1="100" y1="140" x2="85" y2="150" stroke="white" stroke-width="4">
      <animate attributeName="y1" values="140;150;140;" dur="0.7s" repeatCount="indefinite" />
      <animate attributeName="y2" values="150;140;150;" dur="0.7s" repeatCount="indefinite" />
    </line>
    
    <!-- Right Arm -->
    <line x1="100" y1="140" x2="115" y2="130" stroke="white" stroke-width="4">
      <animate attributeName="y1" values="140;130;140;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
      <animate attributeName="y2" values="130;140;130;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
    </line>

    <!-- Add animation keyframes for walking -->
    <animateTransform
      attributeType="XML"
      attributeName="transform"
      type="translate"
      values="0 0; 30 0; 60 0; 90 0; 120 0;"
      dur="2s"
      repeatCount="indefinite"
    />
  </svg>
  </Slide>
<Slide>
  <p>make the leg and the arms attached to the body</p>
  <svg width="200px" height="300px" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <!-- Add your SVG shapes representing the man here -->
  <!-- Body as a line -->
  <line x1="100" y1="130" x2="100" y2="170" stroke="white" stroke-width="6">
    <animate attributeName="y1" values="130;140;130;" dur="1s" repeatCount="indefinite" />
    <animate attributeName="y2" values="170;160;170;" dur="1s" repeatCount="indefinite" />
  </line>
  
  <!-- Head -->
  <circle cx="100" cy="120" r="10" fill="white"/>
  
  <!-- Legs -->
  <!-- Left Leg -->
  <line x1="100" y1="170" x2="100" y2="200" stroke="white" stroke-width="4">
    <animate attributeName="y1" values="170;190;170;" dur="0.7s" repeatCount="indefinite" />
    <animate attributeName="y2" values="200;220;200;" dur="0.7s" repeatCount="indefinite" />
  </line>
  
  <!-- Right Leg -->
  <line x1="100" y1="170" x2="100" y2="200" stroke="white" stroke-width="4">
    <animate attributeName="y1" values="170;190;170;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
    <animate attributeName="y2" values="200;220;200;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
  </line>
  
  <!-- Arms -->
  <!-- Left Arm -->
  <line x1="100" y1="140" x2="85" y2="150" stroke="white" stroke-width="4">
    <animate attributeName="y1" values="140;150;140;" dur="0.7s" repeatCount="indefinite" />
    <animate attributeName="y2" values="150;140;150;" dur="0.7s" repeatCount="indefinite" />
  </line>
  
  <!-- Right Arm -->
  <line x1="100" y1="140" x2="115" y2="130" stroke="white" stroke-width="4">
    <animate attributeName="y1" values="140;130;140;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
    <animate attributeName="y2" values="130;140;130;" dur="0.7s" begin="0.3s" repeatCount="indefinite" />
  </line>

  <!-- Add animation keyframes for walking -->
  <animateTransform
    attributeType="XML"
    attributeName="transform"
    type="translate"
    values="0 0; 30 0; 60 0; 90 0; 120 0;"
    dur="2s"
    repeatCount="indefinite"
  />
</svg>

</Slide>
<Slide>
  <p>Due to the limitations of the text format in this environment, I can provide you with the general idea and keyframes for the walking animation, but I won't be able to present the full SVG animation code here.</p>
  
</Slide>
</Slide>  
