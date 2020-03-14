#include<linux/kernel.h>
#include<linux/module.h>
#include<linux/init.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Shukrithi Rathna");
MODULE_DESCRIPTION("First Hello World Module");

static int __init hello_init(void)
{
    printk(KERN_INFO "Hello world!\n");
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    printk(KERN_INFO "Cleaned up Hello World module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
