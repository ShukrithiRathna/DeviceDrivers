/* Shukrithi Rathna 
   CED16I031
   Device Drivers End Semester Lab Examination

   Write any device driver. Display major and minor number when opened.

*/

//header files
#include<linux/kernel.h>
#include<linux/module.h>
#include<linux/init.h>
#include "device_file.h"
#include <linux/fs.h> 	     /* file stuff */
#include <linux/errno.h>     /* error codes */
#include <linux/cdev.h>      /* char device stuff */
#include <asm/uaccess.h>  /* copy_to_user() */


MODULE_LICENSE("GPL");
MODULE_AUTHOR("Shukrithi Rathna");
MODULE_DESCRIPTION("Hello World Module w/ Device Number");


static const char    g_s_Hello_World_string[] = "Hello world from kernel mode!\n\0";
static const ssize_t g_s_Hello_World_size = sizeof(g_s_Hello_World_string);

static ssize_t device_file_read(struct file *file_ptr , char __user *user_buffer , size_t count , loff_t *position)
{
   printk( KERN_NOTICE "hello_world_driver: Device file is read at offset = %i, read bytes count = %u", (int)*position, (unsigned int)count );

   if( *position >= g_s_Hello_World_size )
      return 0;

   if( *position + count > g_s_Hello_World_size )
      count = g_s_Hello_World_size - *position;
   

   *position += count;
   return count;
}


static struct file_operations simple_driver_fops = 
{
   .owner   = THIS_MODULE,
   .read    = device_file_read,
};

static int device_file_major_number = 0;

static const char device_name[] = "hello_world_driver";


int register_device(void)
{
      int result = 0;

      printk( KERN_NOTICE "hello_world_driver: register_device() is called." );

      result = register_chrdev( 0, device_name, &simple_driver_fops );
      if( result < 0 )
      {
         printk( KERN_NOTICE "hello_world_driver:  can\'t register character device with errorcode = %i", result );
         return result;
      }

      device_file_major_number = result;
      printk( KERN_NOTICE "hello_world_driver: registered character device with major number = %i and minor numbers 0...255"
                  , device_file_major_number );

      return 0;
}


void unregister_device(void)
{
   printk( KERN_NOTICE "hello_world_driver: unregister_device() is called" );
   if(device_file_major_number != 0)
   {
      unregister_chrdev(device_file_major_number, device_name);
   }
}

static int __init hello_init(void)
{
   int result = 0;
   printk(KERN_INFO "Hello world!\n");
   result = register_device();
   return result;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    unregister_device();
    printk(KERN_INFO "Cleaned up Hello World module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
