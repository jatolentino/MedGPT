<template>
    <footer class="footer pt-12 lg:pt-[150px]">
		<div class="container mx-auto pb-12 lg:pb-[100px]">
        	<div class="flex flex-col lg:flex-row gap-x-5 gap-y-10">
				<div class="footer_item flex-1">
					<a href="#">
					<div class="flex justify-center lg:justify-normal">
						<h1 class="text-5xl lg:text-left font-bold relative">
						Med<b class="text-accent">Center</b><br />
						</h1>
					</div>
					</a>
					<p class="mb-[20px] mt-[30px]">
					Exceptional Care, Advanced Treatments and Compassionate Support—Your Health is Our Priority
					</p>
					<div class="flex flex-col gap-y-3 mb-10">
					<div class="flex items-center gap-x-[6px]">
						<i class="ri-map-pin-fill text-[24px] text-accent"></i>
						<div>Los Delfines 43622, MI</div>
					</div>
					<div class="flex items-center gap-x-[6px]">
						<i class="ri-mail-fill text-[24px] text-accent"></i>
						<div>consultas@medcenter.lat</div>
					</div>
					<div class="flex items-center gap-x-[6px]">
						<i class="ri-phone-fill text-[24px] text-accent"></i>
						<div>(+51) 43 249 01</div>
					</div>
					</div>
					<div class="flex gap-[14px] text-[30px]">
					<div class="p-[10px] rounded-[10px] shadow-custom2 text-accent-tertiary hover:text-accent cursor-pointer transition-all">
						<i class="ri-facebook-circle-fill"></i>
					</div>
					<div class="p-[10px] rounded-[10px] shadow-custom2 text-accent-tertiary hover:text-accent cursor-pointer transition-all">
						<i class="ri-instagram-line"></i>
					</div>
					<div class="p-[10px] rounded-[10px] shadow-custom2 text-accent-tertiary hover:text-accent cursor-pointer transition-all">
						<i class="ri-twitter-fill"></i>
					</div>
					<div class="p-[10px] rounded-[10px] shadow-custom2 text-accent-tertiary hover:text-accent cursor-pointer transition-all">
						<i class="ri-linkedin-box-fill"></i>
					</div>
					</div>
				</div>
            <div class="footer_item flex-1">
				<h4 class="h4 mb-5">Quick Links</h4>
				<div class="flex gap-x-5">
					<ul class="flex-1 flex flex-col gap-y-5">
						<li><a href="#" class="hover:text-accent transition-all">Home</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Doctors</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Department</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Services</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Blog</a></li>
					</ul>
					<ul class="flex-1 flex flex-col gap-y-5">
						<li><a href="#" class="hover:text-accent transition-all">Our Pricing</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Contact</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Careers</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Faqs</a></li>
						<li><a href="#" class="hover:text-accent transition-all">Privacy Policy</a></li>
					</ul>
				</div>
            </div>
            <div class="footer_item flex-1">
				<h4 class="h4 mb-5">Opening Hours</h4>
				<div class="flex flex-col gap-5">
					<div class="flex-1">
						<div class="flex justify-between items-center border-b pb-[10px]">
						<div>Monday - Thursday</div>
						<div class="text-accent font-medium">8:00 Am - 6:00 Pm</div>
						</div>
					</div>
					<div class="flex-1">
						<div class="flex justify-between items-center border-b pb-[10px]">
						<div>Friday - Saturday</div>
						<div class="text-accent font-medium">10:00 Am - 4:00 Pm</div>
						</div>
					</div>
					<div class="flex-1">
						<div class="flex justify-between items-center border-b pb-[10px]">
						<div>Sunday</div>
						<div class="text-accent font-medium">Emergency Only</div>
						</div>
					</div>
					<div class="flex-1">
						<div class="flex justify-between items-center border-b pb-[10px]">
						<div>Personal</div>
						<div class="text-accent font-medium">7:00 Am - 9:00 Pm</div>
						</div>
					</div>
				</div>
           </div>
         </div>
       </div>
       <div class="py-[30px] border-t">
         <div class="container mx-auto text-center">
           <div class="font-light text-base">&copy; 2024 MedCenter - All rights reserved.</div>
         </div>
       </div>
    </footer>
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

			sr.reveal('.footer_item', {
			interval: 100,
			delay: 100,
			distance: '100px',
			origin: 'bottom'
			});
		});
		}
	}
</script>

<style scoped>
/* Your scoped CSS here */
</style>

  