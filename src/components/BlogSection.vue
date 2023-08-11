<template>
    <section class="blog">
      <div class="container mx-auto">
        <h2 class="blog_title h2 mb-[50px] text-center lg:text-left">
          Our Recents Posts
        </h2>
        <!-- BLOG POST -->
        <div class="flex flex-col lg:flex-row pag-y-6 lg:gap-y-0 items-center
          lg:justify-between mb-[50px]">
          <!-- POST 1 -->
          <div class="blog_post max-w-[420px] shadow-custom2 rounded-[10px]
            overflow-hidden cursor-pointer group">
            <!-- IMG -->
            <div class="relative overflow-hidden">
              <img class="group-hover:scale-110 transition-all duration-500"
                src="../assets/img/post_1.jpg"
                alt="hands" />
              <!-- BADGE -->
              <div class="bg-accent-tertiary absolute bottom-0 left-0 text-white
                text-base tracking-[2.24px] font-medium uppercase py-[6px] px-[18px]">
                Medical
              </div>
            </div>
            <!-- TEXT -->
            <div class="px-5 py-6">
              <!-- DATE -->
              <div class="mb-4">Dec. 21, 2022</div>
              <!-- TITLE -->
              <h4 class="h4 mb-[10px]">Minimally Invasive Surgery Benefits</h4>
              <!-- DECRIPTION -->
              <p class="font-light">Discover how minimally invasive techniques reduce recovery time, minimize scarring, and improve overall outcomes ...
                <a href="#" class="italic underline text-[#4c5354">Read more</a>
              </p>
            </div>
          </div>
          <!-- POST 2 -->
          <div class="blog_post max-w-[420px] shadow-custom2 rounded-[10px]
            overflow-hidden cursor-pointer group">
            <!-- IMG -->
            <div class="relative overflow-hidden">
              <img class="group-hover:scale-110 transition-all duration-500"
                src="../assets/img/post_2.jpg"
                alt="hands" />
              <!-- BADGE -->
              <div class="bg-accent-tertiary absolute bottom-0 left-0 text-white
                text-base tracking-[2.24px] font-medium uppercase py-[6px] px-[18px]">
                Medical
              </div>
            </div>
            <!-- TEXT -->
            <div class="px-5 py-6">
              <!-- DATE -->
              <div class="mb-4">Jun. 3, 2023</div>
              <!-- TITLE -->
              <h4 class="h4 mb-[10px]">Understanding Plastic Surgery Procedures</h4>
              <!-- DECRIPTION -->
              <p class="font-light">Explore various plastic surgery options, including cosmetic and reconstructive procedures ...
                <a href="#" class="italic underline text-[#4c5354">Read more</a>
              </p>
            </div>
          </div>
          <!-- POST 3 -->
          <div class="blog_post max-w-[420px] shadow-custom2 rounded-[10px]
            overflow-hidden cursor-pointer group">
            <!-- IMG -->
            <div class="relative overflow-hidden">
              <img class="group-hover:scale-110 transition-all duration-500"
                src="../assets/img/post_3.jpg"
                alt="hands" />
              <!-- BADGE -->
              <div class="bg-accent-tertiary absolute bottom-0 left-0 text-white
                text-base tracking-[2.24px] font-medium uppercase py-[6px] px-[18px]">
                Medical
              </div>
            </div>
            <!-- TEXT -->
            <div class="px-5 py-6">
              <!-- DATE -->
              <div class="mb-4">Oct. 17, 2023</div>
              <!-- TITLE -->
              <h4 class="h4 mb-[10px]">Post-Surgery Recovery Tips & Tricks</h4>
              <!-- DECRIPTION -->
              <p class="font-light">Description: Get essential tips for a smooth recovery after surgery. From managing pain to following aftercare ...
                <a href="#" class="italic underline text-[#4c5354">Read more</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
      export default {
          mounted() {
              // Initialize ScrollReveal
              import('scrollreveal').then(ScrollReveal => {
              const sr = ScrollReveal.default({
                  origin: 'bottom',
                  distance: '30px',
                  duration: 1000,
                  delay: 100
              });
  
              sr.reveal('.blog', {interval: 200});
              sr.reveal('.blog_post', {interval: 200});
  
              });
          }
      }
  </script>
  
  <style scoped>
  /* Your scoped CSS here */
  </style>
  