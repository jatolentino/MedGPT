<template>
    <section class="services">
        <div class="bg-accent max-w-[1466px] mx-4 lg:mx-auto rounded-[20px] 
        lg:pt-[70px] px-6 lg:px-0 relative h-[368px] flex items-center lg:items-start -z-10">
            <div class="container mx-auto">
                <div class="services_top flex items-center flex-col lg:flex-row lg:mb-[60px] ">
                <h2 class="h2 text-white flex-1 mb-4 lg:mb-0 text-center lg:text-left ">Your Trusted Partner in Advanced Healthcare</h2>
                <p class="text-white flex-1 text-center lg:text-left
                ">
                We provide timely and specialized medical care tailored to your unique needs. Our team of dedicated professionals combines advanced technology with compassionate support to ensure you receive the highest quality treatment </p>
                </div>
            </div>
        </div>
    </section>
    
    <div class="container mx-auto mt-8 lg:-mt-[144px]">
        <div class="grid lg:grid-cols-4 gap-5 px-8 lg:px-0">
            <div class="services_item bg-white p-[30px] rounded-[10px] 
                shadow-custom2 min-h-[288px] flex flex-col items-center text-center">
                <div class="mb-[15px]">
                <i class="ri-home-8-fill text-6xl text-accent-tertiary"></i>
                </div>
                <h3 class="h3 mb-[10px]">General Practioners</h3>
                <p class="font-light leading-normal max-w-[300px]">
                Comprehensive primary care and health management services
                </p>
            </div>
            <div class="services_item bg-white p-[30px] rounded-[10px] 
                shadow-custom2 min-h-[288px] flex flex-col items-center text-center">
                <div class="mb-[15px]">
                <i class="ri-nurse-fill text-6xl text-accent-tertiary"></i>
                </div>
                <h3 class="h3 mb-[10px]">Online Consultation</h3>
                <p class="font-light leading-normal max-w-[300px]">
                Remote medical advice via virtual on-demand appointments
                </p>
            </div>
            <div class="services_item bg-white p-[30px] rounded-[10px] 
                shadow-custom2 min-h-[288px] flex flex-col items-center text-center">
                <div class="mb-[15px]">
                <i class="ri-article-fill text-6xl text-accent-tertiary"></i>
                </div>
                <h3 class="h3 mb-[10px]">Medical <br/>Support</h3>
                <p class="font-light leading-normal max-w-[300px]">
                Assistance with diagnosis, treatment, and health management
                </p>
            </div>
            <div class="services_item bg-white p-[30px] rounded-[10px] 
                shadow-custom2 min-h-[288px] flex flex-col items-center text-center">
                <div class="mb-[15px]">
                <i class="ri-first-aid-kit-fill text-6xl text-accent-tertiary"></i>
                </div>
                <h3 class="h3 mb-[10px]">Pharmaceutical Care</h3>
                <p class="font-light leading-normal max-w-[300px]">
                    Medication management and drug-related health advice
                </p>
            </div>
        </div>
  </div>
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

            sr.reveal('.services', {interval: 200});
            sr.reveal('.services_top', {interval: 200});
            sr.reveal('.services_item', {interval: 200});
            });
        }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
