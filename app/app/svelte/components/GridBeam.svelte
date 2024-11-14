<script lang="ts">
    import { type ClassValue, clsx } from "clsx";
    import { twMerge } from "tailwind-merge";
    import { M, Motion, useAnimation  } from "svelte-motion";
    import { sleep } from "@sveu/shared"
    

    function cn(...inputs: ClassValue[]) {
        return twMerge(clsx(inputs));
    }
    
  
    let className: any = "";
    export { className as class };
    var opacity1 = 1;
    var opacity2 = 0;
    let controls1 = useAnimation();
    let controls2 = useAnimation();
    var animation = {
      x1: "0%",
      x2: "10%",
      y1: "-40%",
      y2: "-20%",
      transition: {
        duration: 10,
        repeatType: "reverse",
        repeat: Infinity,
      }
    };
    controls1.start(animation);


  </script>
  
  <div class={cn("relative w-full h-full", className)}>
    <svg
      width="100%"
      height="100%"
      viewBox="15 13 25 25"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      class="absolute top-0 left-0"
      opacity={opacity1 == 1 ? '1' : '0'}
    >


    <path
      d="M75,55 L70,55 L70,50 L65,50 L65,45 L60,45 L60,40 L55,40 L55,35"
      stroke="url(#grad1)"
      stroke-width={0.1}
    />
    <path
      d="M65,55 L60,55 L60,50 L55,50 L55,45 L50,45 L50,40 L45,40 L45,35"
      stroke="url(#grad1)"
      stroke-width={0.1}
    />
    <path
      d="M55,55 L50,55 L50,50 L45,50 L45,45 L40,45 L40,40 L35,40 L35,35"
      stroke="url(#grad1)"
      stroke-width={0.1}
    />
    <path
      d="M45,55 L40,55 L40,50 L35,50 L35,45 L30,45 L30,40 L25,40 L25,35"
      stroke="url(#grad1)"
      stroke-width={0.1}
    />



      <path
        d="M50,30 L45,30 L45,25 L40,25 L40,20 L35,20 L35,15 L30,15 L30,10"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M70,50 L65,50 L65,45 L60,45 L60,40 L55,40 L55,35 L50,35 L50,30"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M40,30 L35,30 L35,25 L30,25 L30,20 L25,20 L25,15 L20,15 L20,10"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M60,50 L55,50 L55,45 L50,45 L50,40 L45,40 L45,35 L40,35 L40,30"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M30,30 L25,30 L25,25 L20,25 L20,20 L15,20 L15,15 L10,15 L10,10"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M50,50 L45,50 L45,45 L40,45 L40,40 L35,40 L35,35 L30,35 L30,30"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />

      <path
        d="M20,30 L15,30 L15,25 L10,25 L10,20 L5,20 L5,15 L0,15 L0,10"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />

      <path
        d="M40,50 L35,50 L35,45 L30,45 L30,40 L25,40 L25,35 L20,35 L20,30"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />

      <path
        d="M45,25 L40,25 L40,20 L35,20 L35,15 L30,15 L30,10 L25,10 L25,5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M65,45 L60,45 L60,40 L55,40 L55,35 L50,35 L50,30 L45,30 L45,25"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M35,25 L30,25 L30,20 L25,20 L25,15 L20,15 L20,10 L15,10 L15,5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M55,45 L50,45 L50,40 L45,40 L45,35 L40,35 L40,30 L35,30 L35,25"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M25,25 L20,25 L20,20 L15,20 L15,15 L10,15 L10,10 L5,10 L5,5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M45,45 L40,45 L40,40 L35,40 L35,35 L30,35 L30,30 L25,30 L25,25"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M15,25 L10,25 L10,20 L5,20 L5,15 L0,15 L0,10 L-5,10 L-5,5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M35,45 L30,45 L30,40 L25,40 L25,35 L20,35 L20,30 L15,30 L15,25"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />


      <path
        d="M40,20 L35,20 L35,15 L30,15 L30,10 L25,10 L25,5 L20,5 L20,0"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M60,40 L55,40 L55,35 L50,35 L50,30 L45,30 L45,25 L40,25 L40,20"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M30,20 L25,20 L25,15 L20,15 L20,10 L15,10 L15,5 L10,5 L10,0"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M50,40 L45,40 L45,35 L40,35 L40,30 L35,30 L35,25 L30,25 L30,20"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M20,20 L15,20 L15,15 L10,15 L10,10 L5,10 L5,5 L0,5 L0,0"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M40,40 L35,40 L35,35 L30,35 L30,30 L25,30 L25,25 L20,25 L20,20"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M10,20 L5,20 L5,15 L0,15 L0,10 L-5,10 L-5,5 L-10,5 L-10,0"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M30,40 L25,40 L25,35 L20,35 L20,30 L15,30 L15,25 L10,25 L10,20"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />


      <path
        d="M35,15 L30,15 L30,10 L25,10 L25,5 L20,5 L20,0 L15,0 L15,-5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M55,35 L50,35 L50,30 L45,30 L45,25 L40,25 L40,20 L35,20 L35,15"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M25,15 L20,15 L20,10 L15,10 L15,5 L10,5 L10,0 L5,0 L5,-5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M45,35 L40,35 L40,30 L35,30 L35,25 L30,25 L30,20 L25,20 L25,15"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M15,15 L10,15 L10,10 L5,10 L5,5 L0,5 L0,0 L-5,0 L-5,-5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M35,35 L30,35 L30,30 L25,30 L25,25 L20,25 L20,20 L15,20 L15,15"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M5,15 L0,15 L0,10 L-5,10 L-5,5 L-10,5 L-10,0 L-15,0 L-15,-5"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />
      <path
        d="M25,35 L20,35 L20,30 L15,30 L15,25 L10,25 L10,20 L5,20 L5,15"
        stroke="url(#grad1)"
        stroke-width={0.1}
      />

      

      

      


      <defs>
        <M.linearGradient />
        <Motion
          variants={{
            initial: {
              x1: "100%",
              x2: "100%",
              y1: "100%",
              y2: "100%",
            },
            animate: {
              x1: "0%",
              x2: "0%",
              y1: "-40%",
              y2: "-20%",
            },
          }}
          initial="initial"
          isSVG={true}
          let:motion
          animate={controls1}
        >
          <linearGradient id="grad1" use:motion>
            <stop stop-color="#66F217" stop-opacity="0" />
            <stop stop-color="#66F217" />
            <stop offset="0" stop-color="#58d90d" />
            <stop offset="4" stop-color="#00cc99" stop-opacity="0" />
          </linearGradient>
        </Motion>
      </defs>
    </svg>
    <slot>Helo</slot>
  </div>