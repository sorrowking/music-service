import { ListboxWrapperProps } from "@/types";


export const ListboxWrapper = ({children} : ListboxWrapperProps) => (
  <div className="w-[260px] border-small px-1 py-2 rounded-small border-default-200 dark:border-default-100">
    {children}
  </div>
);