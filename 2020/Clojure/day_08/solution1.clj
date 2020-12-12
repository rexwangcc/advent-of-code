(ns day_08.solution1
  (:require [clojure.string :as str]))


(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(destruct
            [line]
            (let [[operation argument] (str/split line #" ")]
              [operation (read-string argument)]))]
    (->> file
         slurp
         str/split-lines
         (map destruct))))

(defn boot
  "Run all instructions until repetition. Use `mapv` since we need to index the
   index so cannot use lazy-sequence."
  [inputs]
  (letfn [(dispatch [[operation argument]]
                    (case operation
                      "jmp" [argument 0]
                      "nop" [1 0]
                      "acc" [1 argument]))
          (标注 [m] (zipmap (keys m) (repeat true)))]
    (let [inputs->map (mapv (fn [instruction] {instruction false}) inputs)]
      (loop [inputs->map inputs->map
             idx 0
             accumulator 0]
        (if (first (vals (get inputs->map idx)))
          ;; second round detected
          accumulator
          ;; still the first round
          (let [k (first (keys (get inputs->map idx)))
                [Δidx Δaccu] (dispatch k)]
            (recur (update-in inputs->map [idx] 标注)
                   (+ idx Δidx)
                   (+ accumulator Δaccu))))))))

(comment
  (boot (get-lines "./day_08/inputs.txt"))
)
